# Real-Time Fraud Risk Platform

## Overview

A Python-based data engineering project that simulates a real-time fraud detection platform.

The platform:

* Generates transaction events
* Publishes events to Kafka
* Consumes transactions from Kafka
* Performs data quality validation
* Calculates fraud risk scores
* Stores scored transactions
* Exposes a REST API
* Includes automated tests

---

## Architecture

```text
Transaction Producer
        ↓
Kafka Topic
        ↓
Kafka Consumer
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
* Apache Kafka
* Docker
* FastAPI
* Pytest
* Git / GitHub

---

## Project Structure

```text
real-time-fraud-risk-platform/

├── api/
├── consumer/
├── producer/
├── rules/
├── tests/
├── data/
├── docker-compose.yml
├── requirements.txt
└── README.md
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

| Score | Risk Band |
| ----- | --------- |
| 0-39  | LOW       |
| 40-69 | MEDIUM    |
| 70+   | HIGH      |

---

## Start Kafka

```bash
docker compose up -d
```

Verify:

```bash
docker ps
```

---

## Run Producer

Publishes transactions to Kafka.

```bash
python -m producer.kafka_producer
```

---

## Run Consumer

Consumes transactions from Kafka, validates and scores them.

```bash
python -m consumer.kafka_consumer
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

## What This Project Demonstrates

* Event-driven architecture
* Real-time data ingestion
* Kafka producer/consumer pattern
* Data quality validation
* Business rule processing
* REST API development
* Automated testing
* Containerised infrastructure using Docker

---

## Future Enhancements

* PySpark Structured Streaming
* Bronze / Silver / Gold architecture
* PostgreSQL persistence
* CI/CD with GitHub Actions
* Grafana monitoring
* Cloud deployment

```
```
