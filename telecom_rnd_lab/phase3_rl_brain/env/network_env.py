"""Lightweight telecom control environment (no external RL framework required).

State space:
[latency_ms, packet_loss_pct, throughput_mbps, congestion_pct, node_health]

Action space (discrete):
0 reroute traffic
1 adjust bandwidth
2 modify QoS
3 scale edge
4 change routing weights
"""

from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass
class LabState:
    latency_ms: float = 70.0
    packet_loss_pct: float = 0.5
    throughput_mbps: float = 400.0
    congestion_pct: float = 40.0
    node_health: float = 85.0


class ActionSpace:
    def __init__(self, n: int):
        self.n = n


class TelecomEnv:
    def __init__(self) -> None:
        self.action_space = ActionSpace(5)
        self.state = LabState()

    def _as_array(self):
        return [
            self.state.latency_ms,
            self.state.packet_loss_pct,
            self.state.throughput_mbps,
            self.state.congestion_pct,
            self.state.node_health,
        ]

    def reset(self, seed=None, options=None):
        self.state = LabState(
            latency_ms=random.uniform(40, 120),
            packet_loss_pct=random.uniform(0.1, 2.0),
            throughput_mbps=random.uniform(200, 900),
            congestion_pct=random.uniform(20, 70),
            node_health=random.uniform(65, 95),
        )
        return self._as_array(), {}

    def step(self, action: int):
        if action == 0:
            self.state.latency_ms *= 0.90
            self.state.packet_loss_pct *= 0.85
        elif action == 1:
            self.state.throughput_mbps *= 1.08
            self.state.congestion_pct *= 0.95
        elif action == 2:
            self.state.packet_loss_pct *= 0.80
            self.state.latency_ms *= 0.95
        elif action == 3:
            self.state.node_health = min(100, self.state.node_health + 6)
            self.state.congestion_pct *= 0.88
        elif action == 4:
            self.state.latency_ms *= 0.92
            self.state.congestion_pct *= 0.90

        self.state.latency_ms += random.uniform(-4, 9)
        self.state.packet_loss_pct += random.uniform(-0.08, 0.15)
        self.state.throughput_mbps += random.uniform(-20, 25)
        self.state.congestion_pct += random.uniform(-3, 5)
        self.state.node_health += random.uniform(-2, 1)

        self.state.latency_ms = max(1, self.state.latency_ms)
        self.state.packet_loss_pct = max(0, self.state.packet_loss_pct)
        self.state.throughput_mbps = max(1, self.state.throughput_mbps)
        self.state.congestion_pct = min(100, max(0, self.state.congestion_pct))
        self.state.node_health = min(100, max(0, self.state.node_health))

        sla_penalty = 20 if self.state.latency_ms > 120 or self.state.packet_loss_pct > 1.5 else 0
        energy_penalty = 3 if action == 3 else 0
        reward = (
            -0.03 * self.state.latency_ms
            -2.0 * self.state.packet_loss_pct
            +0.01 * self.state.throughput_mbps
            -0.02 * self.state.congestion_pct
            +0.04 * self.state.node_health
            -sla_penalty
            -energy_penalty
        )

        terminated = False
        truncated = False
        return self._as_array(), float(reward), terminated, truncated, {}
