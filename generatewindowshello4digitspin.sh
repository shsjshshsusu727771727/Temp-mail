#!/bin/bash
# Script to generate a random 4-digit Windows Hello style PIN

# Generate a random number between 0 and 9999
random_number=$(( RANDOM % 10000 ))

# Format the number to be exactly 4 digits with leading zeros if necessary
pin=$(printf "%04d" "$random_number")

# Output the generated PIN
echo "Generated Windows Hello 4-digit PIN: $pin"
