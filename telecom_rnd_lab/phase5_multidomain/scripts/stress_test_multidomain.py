"""Run simultaneous satellite, maritime, and urban stress episodes against RL environment."""

from __future__ import annotations

import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from phase3_rl_brain.agents.q_learning_agent import QLearningAgent
from phase3_rl_brain.env.network_env import TelecomEnv


DOMAIN_PROFILES = {
    "satellite": {"latency_bias": 35.0, "loss_bias": 0.5, "throughput_bias": -120.0},
    "maritime": {"latency_bias": 20.0, "loss_bias": 0.7, "throughput_bias": -80.0},
    "urban6g": {"latency_bias": -10.0, "loss_bias": -0.1, "throughput_bias": 180.0},
}


def apply_profile(obs, domain: str):
    profile = DOMAIN_PROFILES[domain]
    return [
        max(1.0, obs[0] + profile["latency_bias"] + random.uniform(-8, 8)),
        max(0.0, obs[1] + profile["loss_bias"] + random.uniform(-0.2, 0.2)),
        max(1.0, obs[2] + profile["throughput_bias"] + random.uniform(-30, 30)),
        min(100.0, max(0.0, obs[3] + random.uniform(5, 20))),
        min(100.0, max(0.0, obs[4] + random.uniform(-8, 2))),
    ]


def run_stress_test(episodes: int = 30, steps: int = 80) -> None:
    env = TelecomEnv()
    agent = QLearningAgent(actions=env.action_space.n, epsilon=0.1)

    for ep in range(episodes):
        obs, _ = env.reset()
        total_reward = 0.0
        for step in range(steps):
            domain = ["satellite", "maritime", "urban6g"][step % 3]
            obs = apply_profile(obs, domain)
            action = agent.act(obs)
            next_obs, reward, *_ = env.step(action)
            agent.learn(obs, action, reward, next_obs)
            obs = next_obs
            total_reward += reward
        print(f"[stress] episode={ep+1}/{episodes} total_reward={total_reward:.2f}")


if __name__ == "__main__":
    run_stress_test()
