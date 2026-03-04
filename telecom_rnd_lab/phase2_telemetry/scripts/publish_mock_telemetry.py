"""Publish synthetic telemetry events into Redpanda/Kafka topic."""

import json
import random
import time

from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda d: json.dumps(d).encode("utf-8"),
)

while True:
    payload = {
        "latency_ms": random.uniform(10, 120),
        "throughput_mbps": random.uniform(50, 900),
        "packet_loss_pct": random.uniform(0, 2),
        "jitter_ms": random.uniform(1, 30),
        "node_cpu_pct": random.uniform(20, 85),
    }
    producer.send("network.telemetry.raw", payload)
    producer.flush()
    print(f"published: {payload}")
    time.sleep(1)
