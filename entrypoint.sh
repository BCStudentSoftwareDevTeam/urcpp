#!/bin/bash
set -e

# Wait for the volume to be mounted
while [ ! -f /home/vscode/urcpp/setup.sh ]; do
    echo "Waiting for volume to be mounted..."
    sleep 1
done

# Run setup.sh
cd /home/vscode/urcpp || { echo "Directory for project not found! Exiting."; exit 1; }
./setup.sh
exec "$@"
