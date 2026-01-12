#!/bin/bash

# Bruteforce script to try all 4-digit PINs from 0000 to 9999

for pin in $(seq -w 0000 9999); do
    echo "Trying PIN: $pin"
    # Here you can add the command to test the PIN, for example:
    # ./test_pin_command $pin
done
