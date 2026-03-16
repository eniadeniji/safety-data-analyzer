from flask import Flask, jsonify
from analysis_engine import *
import json

app = Flask(__name__)

# Load analysis results
def load_results():
    with open("output/analysis_results.json") as f:
        return json.load(f)

# Endpoint: full results
@app.route("/api/results")
def results():
    data = load_results()
    return jsonify(data)

# Endpoint: most dangerous plant
@app.route("/api/most-dangerous-plant")
def dangerous_plant():
    data = load_results()
    return jsonify({
        "most_dangerous_plant": data["most_dangerous_plant"]
    })

# Endpoint: top dangerous days
@app.route("/api/top-dangerous-days")
def dangerous_days():
    data = load_results()
    return jsonify({
        "top_dangerous_days": data["top_dangerous_days"]

    })

@app.route("/")
def home():
    return {
        "message": "Safety Data Analysis API",
        "endpoints": [
            "/api/results",
            "/api/most-dangerous-plant",
            "/api/top-dangerous-days"
        ]
    }

@app.route("/api/risk-scores")
def risk_scores():
    scores = get_plant_risk_scores()
    result = {}

    for location, score in scores:
        result[location] = score

    return jsonify(result)

@app.route("/api/incident-summary")
def incident_summary():
    data = load_data()

    summary = {
        "total_incidents": len(data),
        "high_severity": int ((data["severity"] == "High").sum()),
        "medium_severity": int((data["severity"] == "Medium").sum()),
        "low_severity": int((data["severity"] == "Low").sum())   
    }
    return jsonify(summary)

@app.route("/api/trend")
def trend():
    data = load_data()
    incidents_per_day = data.groupby("date").size()
    result = {
        str(date): int(count)
        for date, count in
    incidents_per_day.items()
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)