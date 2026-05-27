# 🌦️ Weather ETL Data Pipeline (Open-Meteo)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![ETL](https://img.shields.io/badge/ETL-Pipeline-green)
![Status](https://img.shields.io/badge/Status-Production%20Style-orange)
![CI Ready](https://img.shields.io/badge/CI-GitHub%20Actions-lightgrey)

---

## 📌 Project Overview

This project is a **production-style ETL pipeline** built in Python that extracts weather data from a public API, processes it through a structured transformation layer, validates data quality, and outputs curated datasets locally.

It simulates a **real-world Data Engineering workflow** with modular architecture, logging, validation gates, and CI-ready structure.

---

## 🎯 Why this project exists

This project was built to demonstrate practical Data Engineering skills:

- Designing modular ETL pipelines
- Working with external APIs
- Implementing data validation layers
- Adding observability (logging, metrics, previews)
- Structuring CI-ready codebases
- Simulating production data workflows

---

## 🏗️ Architecture

```text
Open-Meteo API
        ↓
   Extract Layer
        ↓
   Transform Layer
      ├── Clean
      ├── Enrich
      └── Validate
        ↓
   Load Layer (Local JSON)
        ↓
Observability Layer
      ├── Logging
      ├── Data Validation
      ├── Data Preview
      └── Run Summary
```

---

## 📁 Project Structure

```text
DE-Pipeline-Project/
│
├── src/
│   ├── extract/        # Data ingestion layer
│   ├── transform/      # Data cleaning, enrichment, validation
│   ├── load/           # Data persistence layer
│   └── utils/          # Logging and helpers
│
├── data/
│   ├── raw/
│   └── curated/
│       └── weather.json
│
├── main.py             # Pipeline orchestration
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run
1. Install dependencies
pip install -r requirements.txt

2. Run pipeline
python main.py

## 📊 Output Example

```text
{
  "temperature": 16.6,
  "windspeed": 3.3,
  "weather_code": 1,
  "latitude": 47.0105,
  "longitude": 28.8638,
  "timestamp": "2026-05-27T02:08:45",
  "is_hot": false,
  "wind_level": "low"
}
```

---

## 🧪 Data Quality Layer

The pipeline enforces basic data validation rules:
Temperature range validation
Windspeed thresholds validation
Required fields checks
Output file integrity check

## 📈 Observability Features
Structured logging (no print statements)
Step-by-step pipeline execution trace
Data preview before persistence
Execution summary (duration, metrics)
Post-load file validation

## 🔁 CI/CD Ready (GitHub Actions)
The project is structured to support CI pipelines:
Automated dependency installation
Pipeline execution on push
Execution visibility in CI logs
Output verification in workflow runs

## 🧠 Key Engineering Concepts Demonstrated
Modular ETL architecture design
Separation of concerns (extract / transform / load)
Data validation and quality gates
Observability in data pipelines
API integration patterns
CI-ready project structuring
