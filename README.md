Safety Data Analyzer

Backend analytics system for monitoring and analyzing industrial safety incidents.

Features

- Synthetic incident dataset generator
- SQLite incident database
- Pandas-based analytics engine
- Risk scoring for plant safety
- Incident trend analysis
- JSON export for machine-readable analytics
- Flask API endpoints for backend services
- Chart generation for incident insights

Example Analysis Output

- Total incidents
- Most dangerous plant
- High severity incident rate
- Top 5 most dangerous days
- Incident distribution by plant

Project Structure

src/

- analyzer.py → CLI entry point
- analysis_engine.py → analytics logic
- database.py → database operations
- generate_data.py → synthetic dataset generator

data/

- incidents.db

output/

- generated reports and charts

Run the Project

Generate dataset

python src/analyzer.py generate

Run analysis

python src/analyzer.py analyze

API Endpoints

/api/top-dangerous-days
/api/incident-summary
/api/risk-scores

Tech Stack

Python
Pandas
SQLite
Flask
Matplotlib

Purpose

This project demonstrates backend data analytics pipelines including data generation, storage, processing, reporting, and API exposure.
