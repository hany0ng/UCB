#!/bin/bash

PREFIX=$1
echo "Scanning $PREFIX.0/24..."
echo "---"

for i in $(seq 1 255)
do
TARGET="$PREFIX.$i"
ping -c 1 "$TARGET" > /dev/null 2>&1 && echo "  $TARGET" >> live_hosts.txt || echo "  $TARGET" >> down_hosts.txt
done

echo "The following hosts are UP:" && cat live_hosts.txt
echo "These hosts have been saved to 'live_hosts.txt'."
echo "---"
echo "The following hosts are DOWN:" && cat down_hosts.txt
echo "These hosts have been saved to 'down_hosts.txt'."

#Changed "seq 1 5" to "seq 1 255" after capturing screenshot
