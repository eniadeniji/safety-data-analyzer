import matplotlib.pyplot as plt
import pandas as pd
import sys
from generate_data import generate_dataset

def run_analysis():
    # Load dataset
    data = pd.read_csv("data/safety_incidents.csv")

    # Basic overview
    print("\n=== DATASET OVERVIEW ===")
    print(data.head(10))

    # Date
    data["date"] = pd.to_datetime(data["date"])

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

    # Calculate percentage of high severity incidents
    high_percentage = (len(high) / total_incidents) * 100
    print("\n=== HIGH SEVERITY INCIDENT RATE ===")
    print(f"{high_percentage:.2f}% of incidents are high severity")

    # Identify the most dangerous plant
    print("\n=== MOST DANGEROUS PLANT ===")
    most_dangerous_plant = high["location"].value_counts().idxmax()
    print(most_dangerous_plant)

    # Incidents by plant and severity
    print("\n=== INCIDENTS BY PLANT AND SEVERITY ===")
    print(data.groupby("location")["severity"].value_counts())

    # Incidents type per plant
    print("\n=== INCIDENT TYPES PER PLANT ===")
    print(data.groupby("location")["incident_type"].value_counts())

    # Incidents per date
    print("\n=== INCIDENTS PER DATE ===")
    print(data["date"].value_counts())

    # Incident trend over time
    print("\n=== INCIDENT TREND OVER TIME ===")
    incidents_per_day = data.groupby("date").size()
    print(incidents_per_day)

    # Identify the top 5 most dangerous days
    # Sort incident counts in descending order
    top_dangerous_days = incidents_per_day.sort_values(ascending=False).head(5)

    print("\n=== TOP 5 MOST DANGEROUS DAYS ===")
    print(top_dangerous_days)

    plt.figure()

    plt.plot(incidents_per_day.index, incidents_per_day.values)

    plt.title("Incident Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Incidents")

    # Save the chart to the output folder
    plt.savefig("output/incidents_trend.png")

    # Close the figure to freee memory
    plt.close()

    # Visualization
    print("\n=== INCIDENTS PER PLANT (CHART) ===")

    plant_counts = data["location"].value_counts()

    plt.figure()  # ← add this

    plt.bar(plant_counts.index, plant_counts.values)

    plt.title("Incidents per Plant")
    plt.xlabel("Plant Location")
    plt.ylabel("Number of Incidents")

    # Save the chart to the output folder
    plt.savefig("output/incidents_per_plant.png")

    # Close the figure to free memory
    plt.close()

    # Severity distribution pie chart
    print("\n=== SEVERITY DISTRIBUTION CHART ===")

    # Count severity levels
    severity_counts = data["severity"].value_counts()

    # Create a pie chart
    plt.figure()

    plt.pie(
        severity_counts.values,
        labels=severity_counts.index,
        autopct="%1.1f%%"
    )

    plt.title("Severity Distribution")

    # Save chart
    plt.savefig("output/severity_distribution.png")

    plt.close()

    # Export report section
    report = []

    report.append("SAFETY INCIDENT ANALYSIS REPORT\n")
    report.append(f"Total incidents: {total_incidents}\n\n")

    report.append("Incidents by location:\n")
    report.append(str(data["location"].value_counts()))
    report.append("\n\n")

    report.append("Severity distribution:\n")
    report.append(str(data["severity"].value_counts()))
    report.append("\n\n")

    # Add top 5 dangerous days to the report
    report.append("Top 5 most dangerous days:\n")
    report.append(str(top_dangerous_days))
    report.append("\n\n")

    # Add most dangerous plant to the report
    report.append(f"Most dangerous plant: {most_dangerous_plant}\n\n")

    report.append(f"High severity incident rate: {high_percentage:.2f}%\n\n")

    with open("output/report.txt", "w") as f:
        f.write("\n".join(report))

    print("\nReport exported to output/report.txt")

# CLI entry point

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage:")
        print("python src/analyzer.py analyze")
        sys.exit()

    command = sys.argv[1]

    if command == "analyze":
        run_analysis()

    elif command == "generate":
        generate_dataset()
        
    else:
        print("Unknown command")
        