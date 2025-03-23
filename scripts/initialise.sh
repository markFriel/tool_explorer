#!/usr/bin/env bash
set -euo pipefail

echo "----------------------------------------"
echo "Step 1: Checking for UV installation..."
if ! command -v uv >/dev/null 2>&1; then
    echo "UV is not installed. Installing UV..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
else
    echo "UV is already installed."
fi

echo "----------------------------------------"
echo "Step 2: Building project from lockfile using UV..."
uv init

echo "----------------------------------------"
echo "Step 3: Copying .env.example to .env..."
if [ -f ".env.example" ]; then
    cp .env.example .env
    echo "Copied .env.example to .env."
else
    echo "Warning: .env.example file not found!"
fi

echo "----------------------------------------"
echo "Step 4: Deleting .env.example file..."
rm -f .env.example && echo "Deleted .env.example file."

echo "----------------------------------------"
echo "Step 5: Checking for pre-commit installation..."
if ! command -v pre-commit >/dev/null 2>&1; then
    echo "pre-commit is not installed. Installing pre-commit..."
    pip install pre-commit
else
    echo "pre-commit is already installed."
fi

echo "----------------------------------------"
echo "Step 6: Initialising pre-commit hooks..."
pre-commit install

echo "----------------------------------------"
echo "Project initialisation complete."
