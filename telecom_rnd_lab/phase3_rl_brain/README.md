# Phase 3 — Reinforcement Learning Brain

## State Space
`[latency, packet_loss, throughput, congestion, node_health]`

## Action Space
0 reroute traffic, 1 adjust bandwidth, 2 modify QoS, 3 scale edge, 4 change routing weights

## Reward
Minimize latency/loss/congestion, keep SLA, penalize expensive scaling.

## Observability
- Exposes Prometheus metrics on port `8000` by default:
  - `rl_episode_reward`
  - `rl_mean_reward`
  - `rl_action_total{action="..."}`

## Run
```bash
python scripts/train_agent.py --episodes 100 --steps 100 --metrics-port 8000
```
