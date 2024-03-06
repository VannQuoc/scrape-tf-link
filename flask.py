from flask import Flask, render_template, request
import subprocess
@app.route('/')
def index():
    return ("VannQuocIsMe")

@app.route('/main.py')
def run_main():
    try:
        process = subprocess.Popen(["python", "main.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "main.py executed successfully"
    except Exception as e:
        return f"An error occurred: {str(e)}"
app.run(host='0.0.0.0', port=8080)
