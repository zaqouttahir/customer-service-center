#!/usr/bin/env bash
set -euo pipefail

echo "Removing local artifacts: .venv, db.sqlite3, TODO.md, __pycache__..."
rm -rf .venv
rm -f db.sqlite3
rm -f TODO.md
find . -name "__pycache__" -type d -prune -exec rm -rf {} +
echo "Done."
