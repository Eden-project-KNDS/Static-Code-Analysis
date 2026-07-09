#!/bin/bash

# Define variables for easy configuration
RULES_FILE="python_anti_patterns.yaml"
JSON_OUTPUT="semgrep_results.json"
PYTHON_SCRIPT="parser.py" 

echo "Starting analysis pipeline..."

echo "Running Semgrep..."
semgrep scan --config="$RULES_FILE" --json -o "$JSON_OUTPUT" . || true

# Check if the JSON file was actually created
if [ ! -f "$JSON_OUTPUT" ]; then
    echo "Error: $JSON_OUTPUT was not created. Semgrep may have failed."
    exit 1
fi
echo "Semgrep finished! Data saved to $JSON_OUTPUT"

# Step 3: Run the Python program
echo "Executing Python script..."
if [ -f "$PYTHON_SCRIPT" ]; then
    python3 "$PYTHON_SCRIPT" "$JSON_OUTPUT"
    echo "Pipeline complete!"
else
    echo "Error: Could not find Python script named $PYTHON_SCRIPT"
    exit 1
fi