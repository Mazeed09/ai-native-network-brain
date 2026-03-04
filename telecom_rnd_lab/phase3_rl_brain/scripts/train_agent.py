"""Train baseline RL controller in the simulated telecom lab environment."""

from __future__ import annotations

import argparse
import statistics
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from phase3_rl_brain.agents.q_learning_agent import QLearningAgent
from phase3_rl_brain.env.network_env import TelecomEnv
from phase3_rl_brain.scripts.metrics_exporter import METRICS, start_metrics_server


def train(episodes: int, steps: int, metrics_port: int) -> None:
    start_metrics_server(metrics_port)
    env = TelecomEnv()
    agent = QLearningAgent(actions=env.action_space.n)

    episodic_rewards = []
    for ep in range(episodes):
        obs, _ = env.reset()
        total_reward = 0.0
        for _ in range(steps):
            action = agent.act(obs)
            METRICS.inc_action(action)
            next_obs, reward, *_ = env.step(action)
            agent.learn(obs, action, reward, next_obs)
            obs = next_obs
            total_reward += reward

        episodic_rewards.append(total_reward)
        METRICS.set_episode_reward(total_reward)
        METRICS.set_mean_reward(statistics.mean(episodic_rewards))
        print(f"[train] episode={ep+1}/{episodes} reward={total_reward:.2f}")

    print(
        f"[train] done episodes={episodes} "
        f"mean_reward={statistics.mean(episodic_rewards):.2f} "
        f"max_reward={max(episodic_rewards):.2f}"
    )


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", type=int, default=100)
    parser.add_argument("--steps", type=int, default=100)
    parser.add_argument("--metrics-port", type=int, default=8000)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    train(args.episodes, args.steps, args.metrics_port)
