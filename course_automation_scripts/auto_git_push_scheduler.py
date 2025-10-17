# auto_git_push_scheduler.py
import subprocess
import time
import os

# Path to your auto_git_push.py script
script_path = "/Users/francescapanteli/Desktop/CodingNomads-python-SQL-and-Databases-MySQL/course_automation_scripts/auto_git_push.py"

def run_git_push():
    print("Running auto_git_push.py...")
    try:
        subprocess.run(["python3", script_path], check=True)
        print("auto_git_push.py completed successfully.\n")
    except subprocess.CalledProcessError as e:
        print(f"Error running auto_git_push.py: {e}\n")

def main():
    print("Starting auto_git_push scheduler (runs every 5 minutes)...")
    while True:
        run_git_push()
        # Sleep for 5 minutes (300 seconds)
        time.sleep(300)

if __name__ == "__main__":
    main()