"""Consume telemetry events, derive engineered features, and write to InfluxDB."""

from __future__ import annotations

import json
import os
from typing import Dict

from influxdb_client import InfluxDBClient, Point
from kafka import KafkaConsumer


def build_feature_vector(metric: Dict[str, float]) -> Dict[str, float]:
    latency = float(metric.get("latency_ms", 0.0))
    throughput = float(metric.get("throughput_mbps", 0.0))
    packet_loss = float(metric.get("packet_loss_pct", 0.0))
    jitter = float(metric.get("jitter_ms", 0.0))
    cpu = float(metric.get("node_cpu_pct", 0.0))

    return {
        "latency_throughput_ratio": latency / max(throughput, 1e-3),
        "loss_jitter_index": packet_loss * jitter,
        "health_score": max(0.0, 100.0 - (latency * 0.1 + packet_loss * 8 + cpu * 0.3)),
    }


def main() -> None:
    kafka_servers = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")
    influx_url = os.getenv("INFLUX_URL", "http://localhost:8086")
    influx_token = os.getenv("INFLUX_TOKEN", "telecom-token")
    influx_org = os.getenv("INFLUX_ORG", "telecom-lab")
    influx_bucket = os.getenv("INFLUX_BUCKET", "telemetry")

    consumer = KafkaConsumer(
        "network.telemetry.raw",
        bootstrap_servers=[kafka_servers],
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        auto_offset_reset="latest",
    )

    with InfluxDBClient(url=influx_url, token=influx_token, org=influx_org) as client:
        writer = client.write_api()
        for message in consumer:
            features = build_feature_vector(message.value)
            point = Point("network_features")
            for key, val in features.items():
                point = point.field(key, float(val))
            writer.write(bucket=influx_bucket, org=influx_org, record=point)
            print(f"[feature-worker] wrote features: {features}")


if __name__ == "__main__":
    main()
