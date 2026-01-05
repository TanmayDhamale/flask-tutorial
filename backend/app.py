from flask import Flask, request
from dotenv import load_dotenv
import os   
import pymongo   

load_dotenv()  

Mongo_URI = os.getenv("Mongo_URI")  # Load environment variables from .env file

client =  pymongo.MongoClient(Mongo_URI)  # Use the correct MongoDB connection string

db = client["test"]

collection = db["flask-tutorial"]

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    
   
    form_data = {
        "name": data.get('username'),
        "password": data.get('password'),
        "created_at": data.get('created_at')
    }
    collection.insert_one(form_data)

    name = data.get('username')
    return f"Thank you for signing up, {name}!"

# @app.route('/submit', methods=['POST'])
# def submit():
    # Accept either JSON (Content-Type: application/json) or form-encoded data
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    username = data.get('username') or data.get('name')
    email = data.get('email')
    password = data.get('password')
    created_at = data.get('created_at')

    # Ensure created_at is a serializable string
    if not created_at:
        from datetime import datetime
        created_at = datetime.now().isoformat()

    doc = {
        "username": username,
        "email": email,
        "password": password,
        "created_at": created_at
    }

    collection.insert_one(doc)

    return f"User {username} registered successfully!"

@app.route('/view')
def view():
    users = collection.find()
    user_list = [str(user.get('username') or '<unknown>') for user in users]
    return "<br>".join(user_list)   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True) 