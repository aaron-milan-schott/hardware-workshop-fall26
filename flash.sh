#!/usr/bin/env bash
# Compile the sketch, then upload it to your Arduino.
set -e
cd "$(dirname "$0")"
if [ -z "$ARDUINO_PORT" ]; then
  echo "ARDUINO_PORT is not set. Ask your instructor."; exit 1
fi
arduino-cli compile --fqbn arduino:avr:uno sketch
arduino-cli upload -p "$ARDUINO_PORT" --fqbn arduino:avr:uno sketch
