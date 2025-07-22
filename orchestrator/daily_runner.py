import schedule
import time
import subprocess
import os
from config import BASE_DIR

def run_daily_pipeline():
    print("Running daily pipeline...")
    try:
        subprocess.run(["python", os.path.join(BASE_DIR, "orchestrator", "run_pipeline.py")], check=True)
        print("Daily pipeline completed successfully!\n")
    except subprocess.CalledProcessError as e:
        print(f"Pipeline failed: {e}")

# Scheduled at 10:00 AM daily
schedule.every().day.at("10:00").do(run_daily_pipeline)

print("Daily scheduler started. The pipeline will run every day at 10:00 AM.\n")

while True:
    schedule.run_pending()
    time.sleep(60)
