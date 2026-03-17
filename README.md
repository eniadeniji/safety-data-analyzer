Safety Data Analyzer

Backend analytics system for monitoring and analyzing industrial safety incidents.

- Generates synthetic industrial safety data
- Stores data in SQLite database
- Performs analysis using Pandas
- Generates charts and reports
- Exposes analytics via Flask API
- Supports automated pipeline execution

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
- Automated pipeline for continuous data processing

---

Example Analysis Output

- Total incidents
- Most dangerous plant
- High severity incident rate
- Top 5 most dangerous days
- Incident distribution by plant
- Incident trends over time

---

Project Structure

- src/
  
  - analyzer.py (CLI entry point)
  - analysis_engine.py (analytics logic)
  - database.py (database operations)
  - generate_data.py (dataset generator)
  - server.py (Flask API)
  - scheduler.py (automated pipeline)

- data/
  
  - incidents.db

- output/
  
  - report.txt
  - analysis_results.json
  - charts

- requirements.txt

- README.md

---

Running the Project

- Install dependencies
  
  - pip install -r requirements.txt

- Generate dataset
  
  - python src/analyzer.py generate

- Run analysis
  
  - python src/analyzer.py analyze

- Start API server
  
  - python src/server.py

- Run automated pipeline
  
  - python src/scheduler.py

---

API Endpoints

- GET /api/incident-summary
  
  - Returns total incidents and severity breakdown

- GET /api/risk-scores
  
  - Returns risk score per plant

- GET /api/trend
  
  - Returns incident counts by date

---

Example API Response

- GET /api/risk-scores

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

Purpose

- Demonstrates backend data analytics pipeline
- Covers data generation, storage, analysis, and reporting
- Exposes processed data through REST API
- Simulates real-world automated data processing systems