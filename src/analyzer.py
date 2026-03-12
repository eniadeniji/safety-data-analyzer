import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
data = pd.read_csv("../data/safety_incidents.csv")

# Basic overview
print("\n=== DATASET OVERVIEW ===")
print(data.head(10))

# Total incidents
total_incidents = len(data)
print("\nTotal incidents:", total_incidents)

# Incidents by location
print("\n=== INCIDENTS BY LOCATION ===")
print(data["location"].value_counts())

# Incident type distribution
print("\n=== INCIDENT TYPES ===")
print(data["incident_type"].value_counts())

# Severity distribution
print("\n=== SEVERITY DISTRIBUTION ===")
print(data["severity"].value_counts())

# High severity 
print("\n=== HIGH SEVERITY INCIDENTS BY PLANT ===")
high = data[data["severity"] == "High"]
print(high["location"].value_counts())

# Incidents by plant and severity
print("\n=== INCIDENTS BY PLANT AND SEVERITY ===")
print(data.groupby("location")["severity"].value_counts())

# Incidents type per plant
print("\n=== INCIDENT TYPES PER PLANT ===")
print(data.groupby("location")["incident_type"].value_counts())

# Incidents per date
print("\n=== INCIDENTS PER DATE ===")
print(data["date"].value_counts())

# Visualization
print("\n=== INCIDENTS PER PLANT (CHART) ===")

plant_counts = data["location"].value_counts()

plt.bar(plant_counts.index, plant_counts.values)

plt.title("Incidents per Plant")
plt.xlabel("Plant Location")
plt.ylabel("Number of Incidents")

plt.show()