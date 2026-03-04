"""Safety guardrails for RL actions before execution in network control plane."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass
class SafetyConfig:
    max_latency_ms: float = 200.0
    max_packet_loss_pct: float = 5.0
    min_node_health: float = 40.0


class SafetyGuard:
    def __init__(self, cfg: SafetyConfig):
        self.cfg = cfg

    def evaluate(self, state: Dict[str, float], action: int) -> Tuple[int, Dict[str, str]]:
        """Apply hard policy constraints and fallback logic."""
        reasons = []

        if state["node_health"] < self.cfg.min_node_health and action == 3:
            reasons.append("edge scaling blocked due to low node health")

        if state["latency_ms"] > self.cfg.max_latency_ms:
            reasons.append("latency exceeds policy bound")

        if state["packet_loss_pct"] > self.cfg.max_packet_loss_pct:
            reasons.append("packet loss exceeds policy bound")

        if reasons:
            # Fallback safe action: modify QoS (action=2).
            return 2, {"decision": "fallback", "reasons": "; ".join(reasons)}
        return action, {"decision": "allow", "reasons": "within bounds"}
