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

if __name__ == "__main__":
    app.run(debug=True)