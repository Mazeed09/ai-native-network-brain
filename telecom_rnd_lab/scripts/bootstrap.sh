#!/usr/bin/env bash
set -euo pipefail

# Bootstrap local python environment with support for online, mirror, or offline wheel installs.
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip

# Installation priority:
# 1) local wheelhouse (offline)
# 2) configured package mirror via PIP_INDEX_URL
# 3) default public index
if [[ -d "$ROOT_DIR/wheelhouse" ]]; then
  echo "[bootstrap] Installing from local wheelhouse (offline mode)."
  pip install --no-index --find-links "$ROOT_DIR/wheelhouse" -r requirements.txt
else
  if [[ -n "${PIP_INDEX_URL:-}" ]]; then
    echo "[bootstrap] Installing from configured mirror: $PIP_INDEX_URL"
  else
    echo "[bootstrap] No wheelhouse found; falling back to default package index."
  fi
  pip install -r requirements.txt
fi

echo "[bootstrap] Completed. Activate env: source $ROOT_DIR/.venv/bin/activate"
