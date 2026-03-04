#!/usr/bin/env bash
set -euo pipefail

# Download all dependencies into ./wheelhouse for offline installs.
# Run this once in a network-enabled environment.
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p wheelhouse
python3 -m pip download -r requirements.txt -d wheelhouse

echo "[wheelhouse] Download complete at $ROOT_DIR/wheelhouse"
