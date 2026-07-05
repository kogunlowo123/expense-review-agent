#!/bin/bash
set -euo pipefail
echo "Setting up Expense Review Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
