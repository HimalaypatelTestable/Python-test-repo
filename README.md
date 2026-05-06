# Testable Demo Python

Sample Python project for Testable whitebox metric validation — master branch is the all-passing baseline.

## Overview

This project demonstrates secure, well-tested Python code that exercises positively
against the Testable whitebox tool's full metric suite (lint, complexity, duplication,
SAST, dependency audit, coverage, def-use, and mutation testing).

## Requirements

- Python >= 3.11

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -e .
```

## Running Tests

```bash
pytest
```

## Running Tests with Coverage

```bash
coverage run --branch ssdsdsdsd-m pytest
coverage report -m
coverage json
```

## Project Layout

- `src/testable_demo/` — library modules
- `tests/` — pytest test suite
