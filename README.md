# Reliable Student Feedback JSON Generator

## Overview
A Python project demonstrating structured JSON validation using Pydantic.

## Features
- JSON schema validation
- Invalid output rejection
- Three-attempt retry mechanism
- Simulated repair process
- Typed Python output
- Automated unit tests

## Technologies
- Python
- Pydantic
- JSON
- unittest

## Installation
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run
```bash
python main.py
```

## Tests
```bash
python test_cases.py
python -m unittest test_validation -v
```

## Implementation Note
This version uses simulated local mock responses, not a live AI model. It demonstrates schema validation, rejection of invalid output, and simulated retry and repair without API charges.

## Test Results
Six automated unit tests passed.
