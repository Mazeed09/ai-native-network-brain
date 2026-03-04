"""Simple tabular Q-learning baseline for discrete control actions."""

from __future__ import annotations

import random
from collections import defaultdict


class QLearningAgent:
    def __init__(self, actions: int, alpha: float = 0.15, gamma: float = 0.95, epsilon: float = 0.2):
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = defaultdict(lambda: [0.0] * actions)

    def _bucketize(self, obs):
        # Coarse discretization to keep state table bounded.
        return tuple(int(v // 10) for v in obs)

    def act(self, obs):
        key = self._bucketize(obs)
        if random.random() < self.epsilon:
            return random.randint(0, self.actions - 1)
        return max(range(self.actions), key=lambda a: self.q_table[key][a])

    def learn(self, obs, action, reward, next_obs):
        s = self._bucketize(obs)
        ns = self._bucketize(next_obs)
        best_next = max(self.q_table[ns])
        td_target = reward + self.gamma * best_next
        td_error = td_target - self.q_table[s][action]
        self.q_table[s][action] += self.alpha * td_error
