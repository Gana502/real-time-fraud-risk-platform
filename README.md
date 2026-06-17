# Real-Time Fraud Risk Platform

## Overview

This project simulates a real-time fraud detection platform.

Transactions are generated, validated using data quality rules, scored using fraud detection logic and written to a structured output format.

## Architecture

Transaction Producer
    ↓
Data Quality Validation
    ↓
Fraud Scoring Engine
    ↓
JSONL Output
    ↓
API Layer (Next Phase)

## Technologies

- Python
- Pytest
- FastAPI (coming next)
- Kafka (planned)
- PySpark Structured Streaming (planned)

## Features

- Transaction generation
- Data quality validation
- Fraud risk scoring
- Automated unit testing

## Run

```bash
python producer/transaction_producer.py