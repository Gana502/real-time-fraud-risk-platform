# Real-Time Fraud Risk Platform

## Overview

A Python-based data engineering project that simulates a real-time fraud detection workflow.

The platform:

* Generates transaction events
* Validates data quality
* Calculates fraud risk scores
* Classifies transactions into risk bands
* Exposes a REST API for scoring transactions
* Includes automated tests

---

## Architecture

```text
Transaction Producer
        ↓
Data Quality Validation
        ↓
Fraud Scoring Engine
        ↓
JSONL Output
        ↓
FastAPI Service
```

---

## Tech Stack

* Python
* FastAPI
* Pytest
* Git/GitHub

---

## Project Structure

```text
real-time-fraud-risk-platform/

├── api/
├── producer/
├── rules/
├── tests/
├── data/
├── README.md
└── requirements.txt
```

---

## Features

### Data Quality Checks

* Required field validation
* Null value validation
* Positive amount validation

### Fraud Scoring Rules

| Rule                  | Score |
| --------------------- | ----- |
| Amount > £1000        | +40   |
| Non-UK Transaction    | +25   |
| Online/Mobile Channel | +10   |
| New Device            | +25   |

### Risk Bands

| Score | Band   |
| ----- | ------ |
| 0-39  | LOW    |
| 40-69 | MEDIUM |
| 70+   | HIGH   |

---

## Run Transaction Producer

```bash
python producer/transaction_producer.py
```

Output:

```text
data/transactions_scored.jsonl
```

---

## Run API

```bash
uvicorn api.main:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Run Tests

```bash
python -m pytest -v
```

---

## Sample API Response

```json
{
  "transaction_id": "TXN001",
  "risk_score": 100,
  "risk_band": "HIGH"
}
```

---

## Future Enhancements

* Kafka streaming
* PySpark Structured Streaming
* Docker
* CI/CD with GitHub Actions
* PostgreSQL
* Grafana Monitoring

```
```
