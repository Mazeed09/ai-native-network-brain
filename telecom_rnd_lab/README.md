# Autonomous Digital Telecom R&D Lab

This module provides a **phase-separated**, reproducible scaffold for building a closed-loop telecom experimentation lab.

## Phases
- **Phase 1 — Digital Network Environment**: Open5GS + RAN emulator placeholders, Mininet SDN topology, tc impairment injection, edge/cloud container orchestration, Prometheus + Grafana dashboards.
- **Phase 2 — Telemetry Pipeline**: Redpanda streaming, InfluxDB storage, and feature engineering workers.
- **Phase 3 — Reinforcement Learning Brain**: Q-learning training loop with explicit state/action/reward plus Prometheus metrics export.
- **Phase 4 — Safety & Stability**: Policy constraints, safe bounds, fallback actions, and explainability logs.
- **Phase 5 — Multi-Domain Expansion**: Satellite, maritime mesh, and urban 6G templates with a combined stress harness.

## Quick Start
```bash
cd telecom_rnd_lab
bash scripts/bootstrap.sh
bash scripts/run_phase.sh 1
bash scripts/run_phase.sh 2
python phase3_rl_brain/scripts/train_agent.py --episodes 100 --steps 100 --metrics-port 8000
python phase5_multidomain/scripts/stress_test_multidomain.py
```

## Package Install Options (Fix for Proxy/Network Limits)
- **Offline mode**: preload wheels once and reuse in restricted environments.
  ```bash
  bash scripts/build_wheelhouse.sh     # run where internet is available
  bash scripts/bootstrap.sh            # installs from ./wheelhouse automatically
  ```
- **Local PyPI mirror mode**:
  ```bash
  bash scripts/configure_pip_mirror.sh http://<your-mirror>/simple
  bash scripts/bootstrap.sh
  ```

## Folder Layout
```text
telecom_rnd_lab/
  phase1_digital_env/
  phase2_telemetry/
  phase3_rl_brain/
  phase4_safety/
  phase5_multidomain/
  shared/
  scripts/
```

## Notes
- Every phase can run independently.
- For production-grade deployments, tune security, resource limits, and harden observability pipelines.
