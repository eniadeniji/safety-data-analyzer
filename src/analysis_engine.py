import pandas as pd
import sqlite3

DB_PATH = "data/incidents.db"

def get_most_dangerous_plant():
    conn = sqlite3.connect(DB_PATH)

    query = """ 
    SELECT location, COUNT(*) as high_incidents
    FROM incidents
    WHERE severity = 'High'
    GROUP BY location
    ORDER BY high_incidents DESC
    LIMIT 1
    """

    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result

# Load dataset
def load_data():
    conn = sqlite3. connect(DB_PATH)
    query = "SELECT * FROM incidents"
    data = pd.read_sql_query(query, conn)
    conn.close()
    data["date"] = pd.to_datetime(data["date"])
    return data

# Get top dangerous days
def get_top_dangerous_days(data):
    incidents_per_day = data.groupby("date").size()
    return incidents_per_day.sort_values(ascending=False).head(5)

# Calculate high severity percentage
def get_high_severity_rate(data):
    total_incidents = len(data)
    high = data[data["severity"] == "High"]
    return (len(high) / total_incidents) * 100

# Basic summary stats
def get_summary(data):
    return {
        "total_incidents": len(data),
        "incidents_by_location": data["location"].value_counts(),
        "incidents_types": data["incident_type"].value_counts(),
        "severity_distribution": data["severity"]. value_counts(),
    }

# Get severity scores
def get_plant_risk_scores():
    conn = sqlite3.connect(DB_PATH)
    query = """
    SELECT location,
    sum(
        CASE
            WHEN severity = 'High' THEN 5
            WHEN severity = 'Medium' THEN 3

            ELSE 1
    
        END
    ) AS risk_score
    FROM incidents
    GROUP BY location
    ORDER BY risk_score DESC
    """

    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results