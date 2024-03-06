import time
import subprocess
import requests
import psutil

def run_bot():
    while True:
        print("Starting the bot...")
        process = subprocess.Popen(["python", "flask.py"], stderr=subprocess.PIPE)
        process = subprocess.Popen(["python", "main.py"], stderr=subprocess.PIPE)
        print("Bot running. Waiting before accessing the URL...")
        time.sleep(1800)
        cpu_percent = psutil.cpu_percent(interval=1)
        if cpu_percent > 98.0:
            print(f"CPU usage is high ({cpu_percent}%). Restarting the bot...")
            process.kill()
            continue
        else:
            print(f"CPU usage is {cpu_percent}%.")
        try:
            print("Accessing the website...")
            response = requests.get("https://telesms2.uaxxxxxx.repl.co/main.py")
            if response.status_code == 200:
                print("Website accessed successfully.")
            else:
                print("Failed to access the website.")
        except Exception as e:
            print(f"An error occurred while accessing the website: {e}")

if __name__ == "__main__":
    while True:
        try:
            run_bot()
        except Exception as e:
            print(f"An error occurred while running the bot: {e}")
            print("Restarting the bot after an error...")
            time.sleep(0)
