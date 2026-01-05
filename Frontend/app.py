from flask import Flask, render_template, request
from datetime import datetime
import requests

Backend_URL = "http://localhost:9000"

app = Flask(__name__)

@app.route('/')
def home():

    day_of_week = datetime.now().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    print(day_of_week) 

    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)

@app.route('/submit', methods=['POST'])
def submit():
    # Read fields from the form the browser submits (application/x-www-form-urlencoded)
    username = request.form.get('username')
    password = request.form.get('password')

    form_data = {
        "username": username,
        "password": password,
        "created_at": datetime.now().isoformat()
    }

    # Send JSON to backend (requests will set Content-Type: application/json)
    response = requests.post(f"{Backend_URL}/submit", json=form_data)

    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)