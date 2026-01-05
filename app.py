from flask import Flask, request, render_template
from datetime import datetime
from dotenv import load_dotenv
import os   
import pymongo   

load_dotenv()  

Mongo_URI = os.getenv("Mongo_URI")  # Load environment variables from .env file

client =  pymongo.MongoClient(Mongo_URI)  # Use the correct MongoDB connection string

db = client["test"]

collection = db["flask-tutorial"]

app = Flask(__name__)

@app.route('/')
def home():

    day_of_week = datetime.now().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    print(day_of_week) 

    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)


@app.route('/submit', methods=['POST'])
def submit():
    # The form's input uses name="username" so read that field
    name = request.form.get('username')
   
    form_data = {
        "name": name,
        "password": request.form.get('password'),
        "created_at": datetime.now()
    }

    collection.insert_one(form_data)

    return f"Thank you for signing up, {name}!"

if __name__ == '__main__':
    app.run(debug=True)