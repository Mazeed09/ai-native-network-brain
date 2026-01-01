import pandas as pd

# Load data
df = pd.read_csv("data/network_metrics.csv")

# Classify network state
def classify_state(row):
    if row["packet_loss"] > 2 or row["latency"] > 150:
        return "degraded"
    elif row["packet_loss"] > 1 or row["latency"] > 100:
        return "warning"
    else:
        return "healthy"

df["state"] = df.apply(classify_state, axis=1)

# Show first few rows
print(df[["timestamp", "latency", "packet_loss", "state"]].head())