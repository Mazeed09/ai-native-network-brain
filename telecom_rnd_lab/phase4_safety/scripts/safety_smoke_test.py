"""Smoke test for safety constraints, fallback behavior, and explainability output."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from phase4_safety.explainability.action_explainer import explain
from phase4_safety.policies.safety_guard import SafetyConfig, SafetyGuard


def main() -> None:
    guard = SafetyGuard(SafetyConfig())
    state = {
        "latency_ms": 245.0,
        "packet_loss_pct": 2.7,
        "throughput_mbps": 240.0,
        "congestion_pct": 80.0,
        "node_health": 55.0,
    }
    proposed_action = 4
    safe_action, decision = guard.evaluate(state, proposed_action)
    explanation = explain(safe_action, state)
    print("decision:", decision)
    print("explanation:", explanation)


if __name__ == "__main__":
    main()
