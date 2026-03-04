# Phase 1 — Digital Network Environment

## Includes
- Open5GS + UERANSIM docker services
- Mininet SDN topology (`mininet/topology.py`)
- Linux `tc` profile injector (`scripts/apply_tc_profiles.sh`)
- Edge/cloud K8s deployment templates (`k8s/edge-cloud-nodes.yaml`)
- Prometheus scrape configuration (`prometheus/prometheus.yml`)
- Grafana provisioning and telecom dashboard (`grafana/`)

## Run
```bash
docker compose -f docker/docker-compose.yml up -d
sudo python mininet/topology.py
bash scripts/apply_tc_profiles.sh eth0 70ms 0.4% 15mbit
kubectl apply -f k8s/edge-cloud-nodes.yaml
```

## Access
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000` (default admin/admin)
