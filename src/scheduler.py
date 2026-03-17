import time
from generate_data import generate_dataset
from analyzer import run_analysis

def run_pipeline():
    print("Running scheduled pipeline...")

    # Step 1: generate new data
    generate_dataset()

    # Step 2: run analysis
    run_analysis()

    print("Pipeline completed.\n")

if __name__ == "__main__":
    while True:
        run_pipeline()

        # run every 60 seconds (for demo)
        time.sleep(300)