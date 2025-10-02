#!/bin/bash
set -e

# Run setup.sh
cd /home/vscode/urcpp || { echo "Directory for project not found! Exiting."; exit 1; }
./setup.sh
exec "$@"
