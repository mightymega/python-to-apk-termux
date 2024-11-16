#!/bin/bash

echo "=========================================="
echo "      Python to APK Converter for Termux"
echo "=========================================="

echo "Please provide the path to your Python script:"
read script_path

if [ -f "$script_path" ]; then
    python3 apk_compiler.py "$script_path"
else
    echo "File not found. Please check the path and try again."
fi
