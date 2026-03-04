#!/usr/bin/env bash
set -euo pipefail

# Apply Linux tc shaping on a target interface.
# Example: ./apply_tc_profiles.sh eth0 60ms 0.5% 10mbit

IFACE="${1:-eth0}"
DELAY="${2:-50ms}"
LOSS="${3:-0.2%}"
RATE="${4:-20mbit}"

sudo tc qdisc del dev "$IFACE" root || true
sudo tc qdisc add dev "$IFACE" root handle 1: htb default 10
sudo tc class add dev "$IFACE" parent 1: classid 1:10 htb rate "$RATE"
sudo tc qdisc add dev "$IFACE" parent 1:10 handle 10: netem delay "$DELAY" loss "$LOSS" 25%

echo "[tc] Applied delay=$DELAY loss=$LOSS rate=$RATE on $IFACE"
