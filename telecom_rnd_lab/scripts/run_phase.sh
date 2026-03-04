#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <phase-number>"
  exit 1
fi

PHASE="$1"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

case "$PHASE" in
  1)
    docker compose -f "$ROOT_DIR/phase1_digital_env/docker/docker-compose.yml" up -d
    ;;
  2)
    docker compose -f "$ROOT_DIR/phase2_telemetry/redpanda/docker-compose.yml" up -d
    ;;
  3)
    source "$ROOT_DIR/.venv/bin/activate" || true
    python "$ROOT_DIR/phase3_rl_brain/scripts/train_agent.py" --episodes 100 --steps 100 --metrics-port 8000
    ;;
  4)
    source "$ROOT_DIR/.venv/bin/activate" || true
    python "$ROOT_DIR/phase4_safety/scripts/safety_smoke_test.py"
    ;;
  5)
    source "$ROOT_DIR/.venv/bin/activate" || true
    python "$ROOT_DIR/phase5_multidomain/scripts/run_multidomain_demo.py"
    python "$ROOT_DIR/phase5_multidomain/scripts/stress_test_multidomain.py"
    ;;
  *)
    echo "Unknown phase: $PHASE"
    exit 2
    ;;
esac
