Safety Data Analyzer

Backend analytics system for monitoring and analyzing industrial safety incidents.

This project simulates industrial safety incidents, stores them in a database, performs analytics using Pandas and SQL, generates reports and charts, and exposes the results through a Flask API.

---

Features

- Synthetic incident dataset generator
- SQLite incident database
- Pandas-based analytics engine
- Risk scoring for plant safety
- Incident trend analysis
- JSON export for machine-readable analytics
- Flask API endpoints for backend services
- Chart generation for incident insights

---

Example Analysis Output

The analysis engine calculates:

- Total incidents
- Most dangerous plant
- High severity incident rate
- Top 5 most dangerous days
- Incident distribution by plant
- Incident trends over time

---

Project Structure

safety-data-analyzer
│
├── src
│   ├── analyzer.py          # CLI entry point
│   ├── analysis_engine.py   # analytics logic
│   ├── database.py          # database operations
│   ├── generate_data.py     # synthetic dataset generator
│   └── server.py            # Flask API server
│
├── data
│   └── incidents.db
│
├── output
│   ├── report.txt
│   ├── analysis_results.json
│   └── charts
│
├── requirements.txt
└── README.md

---

Running the Project

Install dependencies

pip install -r requirements.txt

Generate synthetic dataset

python src/analyzer.py generate

Run the analytics engine

python src/analyzer.py analyze

Start the API server

python src/server.py

---

API Endpoints

Incident Summary

GET /api/incident-summary

Returns severity distribution and total incident count.

Risk Scores

GET /api/risk-scores

Returns calculated safety risk scores for each plant.

Incident Trend

GET /api/trend

Returns incident counts grouped by date.

---

Example API Response

GET /api/risk-scores

{
  "Plant D": 137,
  "Plant A": 121,
  "Plant B": 118,
  "Plant C": 103
}

---

Tech Stack

- Python
- Pandas
- SQLite
- Flask
- Matplotlib

---

Architecture

Data Generator
      ↓
SQLite Database
      ↓
Analysis Engine (Pandas + SQL)
      ↓
Reports + Charts
      ↓
Flask API

---

Purpose

This project demonstrates a backend analytics pipeline, including:

- synthetic data generation
- database storage
- analytical processing
- report generation
- REST API exposure

It showcases backend development, data processing, and analytics system design.
