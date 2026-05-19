# FastAPI Cross-Study Benchmarking API

## Project Overview

This project is a FastAPI-based analytics service developed to compare clinical studies using their latest validation metrics.

The application:

* Retrieves latest validation runs for studies
* Calculates phase-wise compliance benchmarks
* Compares study performance against benchmarks
* Supports filtering and validation history retrieval
* Uses MySQL with SQLAlchemy ORM

---

# Technology Stack

* FastAPI
* SQLAlchemy ORM
* MySQL
* Pydantic
* Pytest
* Docker
* Jenkins

---

# Project Structure

```text
FASTAPI_ASSESSMENT/
│
├── routers/
│   └── analytics.py
│
├── tests/
│   ├── conftest.py
│   ├── test_analytics.py
│   └── test_integration.py
│
├── logs/
├── crud_metrics.py
├── database.py
├── logger_config.py
├── main.py
├── models.py
├── schemas.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# Features Implemented

* Cross-study analytics endpoint
* Latest validation metrics retrieval
* Phase-wise benchmark calculation
* Benchmark comparison logic
* Phase filtering
* Validation history retrieval
* Logging support
* Exception handling
* Unit testing using pytest
* Integration testing using FastAPI TestClient
* Docker support
* Jenkins CI/CD pipeline

---

# API Endpoint

## Get Cross-Study Metrics

```http
GET /api/v1/metrics/cross-study
```

### Optional Query Parameters

| Parameter       | Description                      |
| --------------- | -------------------------------- |
| phase           | Filter studies by clinical phase |
| include_history | Include validation run history   |

### Example

```http
GET /api/v1/metrics/cross-study?phase=Phase%20III&include_history=true
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository_url>
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure MySQL Database

Database Name:

```text
sdtm_db
```

Update database configuration in:

```text
database.py
```

---

## 5. Run FastAPI Application

```bash
uvicorn main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

# Running Tests

## Unit & Integration Tests

```bash
pytest
```

---

# Docker Setup

## Build Docker Image

```bash
docker build -t fastapi-assessment .
```

## Run Docker Container

```bash
docker run -d -p 8000:8000 fastapi-assessment
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

# Jenkins Pipeline

Pipeline Stages:

* Clone Repository
* Install Dependencies
* Run Tests
* Build Docker Image
* Run Docker Container

---

# Logging

Application logs are stored in:

```text
logs/app.log
```

---

# Testing

Implemented Using:

* pytest
* FastAPI TestClient

Test Coverage Includes:

* Endpoint testing
* Phase filtering
* Exception handling
* Response validation
* Integration flow

---

# Key Concepts Used

* FastAPI Routing
* SQLAlchemy ORM Relationships
* CRUD Operations
* Benchmark Analytics
* REST API Design
* Docker Containerization
* Jenkins CI/CD Pipeline
* Unit Testing
* Integration Testing

---

# Author

Vijayalakshmi G
