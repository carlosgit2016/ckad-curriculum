#!/bin/bash

set -e
file="pods_output"

echo "===== Canary Deployment 70 ====="
total=$(cat $file | wc -l) # replace file.txt with your actual file name
count=$(grep -c "canary-deployment-70" $file) # replace "my output 1" with your actual pattern
percentage=$(echo "scale=2; $count/$total*100" | bc)
echo "$percentage%"

echo "===== Canary Deployment 30 ====="
total=$(cat $file | wc -l) # replace file.txt with your actual file name
count=$(grep -c "canary-deployment-30" $file) # replace "my output 1" with your actual pattern
percentage=$(echo "scale=2; $count/$total*100" | bc) 
echo "$percentage%"

