# Real-Time Fraud Risk Platform

## Overview

This project demonstrates how to build a simplified real-time fraud detection platform using modern data engineering and DevOps technologies.

The solution simulates transaction events, processes them in real time using Kafka, validates data quality, applies fraud scoring rules and exposes the results through a FastAPI service.

The project also demonstrates containerisation, CI/CD and Kubernetes deployment.

---

## Architecture
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/b8e9d33d-67c5-4444-9ee4-9dc8ada9ffd5" />

---

## Technologies Used
<img width="1622" height="970" alt="image" src="https://github.com/user-attachments/assets/3cfd6a3c-a7d3-499a-a20b-c221ac31cd54" />
---

## Features

* Simulated real-time transaction producer
* Kafka-based event streaming
* Data quality validation
* Rule-based fraud scoring
* REST API using FastAPI
* Automated unit testing using Pytest
* Docker containerisation
* CI/CD using GitHub Actions
* Docker image publishing to GitHub Container Registry
* Kubernetes deployment
* Infrastructure as Code using Terraform

---

## Project Structure

```text
api/
consumer/
producer/
rules/
tests/
data/
k8s/
terraform/
.github/workflows/
```

---

## Running the Project

### 1. Start Kafka

```bash
docker compose up -d
```

### 2. Start the Producer

```bash
python -m producer.kafka_producer
```

### 3. Start the Consumer

```bash
python -m consumer.kafka_consumer
```

### 4. Start the API

```bash
uvicorn api.main:app --reload
```

Open:

```text
http://localhost:8000/docs
```

---

## Running Tests

```bash
python -m pytest -v
```

---

## CI/CD Pipeline

Every push to the GitHub repository automatically triggers GitHub Actions.

The pipeline:

* Installs project dependencies
* Runs automated tests
* Builds a Docker image
* Publishes the image to GitHub Container Registry (GHCR)

---

## Kubernetes Deployment

The application is deployed to Kubernetes using Deployment and Service resources.

Terraform is used to provision and manage the Kubernetes infrastructure.

---

## Future Enhancements

* Structured logging
* Dead Letter Queue (DLQ)
* Monitoring and alerting
* PySpark Structured Streaming
* Machine learning fraud detection
* Cloud deployment (AWS/Azure)

---

## Author

**Gana**
Lead Data Engineer
