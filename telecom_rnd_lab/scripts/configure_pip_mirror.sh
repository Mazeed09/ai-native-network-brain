#!/usr/bin/env bash
set -euo pipefail

# Configure pip to use a local PyPI mirror (devpi/artifactory/nexus).
# Usage: ./configure_pip_mirror.sh http://mirror.local/simple
MIRROR_URL="${1:-}"
if [[ -z "$MIRROR_URL" ]]; then
  echo "Usage: $0 <mirror-simple-index-url>"
  exit 1
fi

mkdir -p "$HOME/.config/pip"
cat > "$HOME/.config/pip/pip.conf" <<CONF
[global]
index-url = ${MIRROR_URL}
timeout = 30
CONF

echo "[pip] Mirror configured: $MIRROR_URL"
