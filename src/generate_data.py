import pandas as pd
import random
from datetime import datetime, timedelta
from database import initialize_database, insert_incident

def generate_dataset():

    # Initialize database
    initialize_database()

    locations = ["Plant A", "Plant B", "Plant C", "Plant D"]

    incident_types = [
        "Equipment Failure",
        "Fire Hazard",
        "Slip",
        "Electrical Issue",
        "Chemical Spill"
    ]

    severities = ["Low", "Medium", "High"]

    descriptions = [
        "Conveyor motor overheated during startup",
        "Smoke detected near curing oven",
        "Operator slipped near wash station",
        "Control panel wiring malfunction",
        "Minor solvent leak detected",
        "Forklift brake response delay",
        "Cooling pump pressure fluctuation",
        "Sensor malfunction halted production",
    ]

    rows = []

    start_date = datetime(2025, 1, 1)

    for i in range(60):  # 60 days of data
        current_date = start_date + timedelta(days=i)

        # random number of incidents each day
        incidents_today = random.randint(1, 10)

        for _ in range(incidents_today):

            date = current_date.strftime("%Y-%m-%d")
            location = random.choice(locations)
            incident_type = random.choice(incident_types)
            severity = random.choices(severities, weights=[0.5, 0.35, 0.15])[0]
            description = random.choice(descriptions)

            rows.append({
                "date": date,
                "location": location,
                "incident_type": incident_type,
                "severity": severity,
                "description": description   
            })

            # Insert into database
            insert_incident(date, location, incident_type, severity, description)

    df = pd.DataFrame(rows)

    df.to_csv("data/safety_incidents.csv", index=False)

    print("Dataset generated:", len(df), "rows")

if __name__ == "__main__":
    generate_dataset()