#!/bin/bash
echo "Version 1.0.0"

# Run the main script
python3 ./scripts/main.py

make main.pdf

make clean
clear

# Check if the optimized_results.csv file is generated
if [ -f "results/optimized_results.csv" ]; then
    echo "Smoke test passed: Optimization script executed successfully."
else
    echo "Smoke test failed: Optimization script did not generate the expected results."
    exit 1
fi

# Check if the main.pdf file is generated
if [ -f "report/main.pdf" ]; then
    echo "Smoke test passed: make main.pdf successfully."
else
    echo "Smoke test failed: make main.pdf did not generate the expected results."
    exit 1
fi
