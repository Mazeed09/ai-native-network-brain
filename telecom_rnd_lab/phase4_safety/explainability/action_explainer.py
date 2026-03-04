"""Action explainability helper for auditability and human review."""

ACTIONS = {
    0: "reroute traffic",
    1: "adjust bandwidth",
    2: "modify QoS profile",
    3: "scale edge resources",
    4: "change routing weights",
}


def explain(action: int, context: dict) -> str:
    action_text = ACTIONS.get(action, "unknown")
    return (
        f"Selected action={action} ({action_text}) based on "
        f"latency={context.get('latency_ms'):.2f}ms, "
        f"loss={context.get('packet_loss_pct'):.2f}%, "
        f"throughput={context.get('throughput_mbps'):.2f}Mbps."
    )
