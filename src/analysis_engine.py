import pandas as pd

# Load dataset
def load_data(filepath):
    data = pd.read_csv(filepath)
    data["date"] = pd.to_datetime(data["date"])
    return data

# Calculate most dangerous plant
def get_most_dangerous_plant(data):
    high = data[data["severity"] == "High"]
    return high["location"].value_counts().idxmax()

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
