# Phase 2 — Telemetry Pipeline

## Includes
- Redpanda + InfluxDB via docker compose
- Mock telemetry publisher
- Feature engineering worker that computes derived KPIs and writes to InfluxDB

## Run
```bash
docker compose -f redpanda/docker-compose.yml up -d
python scripts/publish_mock_telemetry.py
python feature_engineering/feature_worker.py
```
