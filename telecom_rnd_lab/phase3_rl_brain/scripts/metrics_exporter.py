"""Tiny Prometheus-compatible metrics exporter implemented with Python stdlib."""

from __future__ import annotations

from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread


class MetricsStore:
    def __init__(self) -> None:
        self.episode_reward = 0.0
        self.mean_reward = 0.0
        self.action_counts = {str(i): 0 for i in range(5)}

    def inc_action(self, action: int) -> None:
        key = str(action)
        self.action_counts[key] = self.action_counts.get(key, 0) + 1

    def set_episode_reward(self, value: float) -> None:
        self.episode_reward = value

    def set_mean_reward(self, value: float) -> None:
        self.mean_reward = value

    def render(self) -> str:
        lines = [
            "# HELP rl_episode_reward Latest RL episode reward",
            "# TYPE rl_episode_reward gauge",
            f"rl_episode_reward {self.episode_reward}",
            "# HELP rl_mean_reward Running mean reward",
            "# TYPE rl_mean_reward gauge",
            f"rl_mean_reward {self.mean_reward}",
            "# HELP rl_action_total Total RL actions",
            "# TYPE rl_action_total counter",
        ]
        for action, count in self.action_counts.items():
            lines.append(f'rl_action_total{{action="{action}"}} {count}')
        return "\n".join(lines) + "\n"


METRICS = MetricsStore()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/metrics":
            self.send_response(404)
            self.end_headers()
            return
        payload = METRICS.render().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; version=0.0.4")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format, *args):
        return


def start_metrics_server(port: int = 8000) -> None:
    server = HTTPServer(("0.0.0.0", port), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
