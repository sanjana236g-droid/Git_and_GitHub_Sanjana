from flask import Flask, jsonify, request
import json
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient('mongodb://localhost:27017/') 
db = client['todo_database']
collection = db['todo_items']

@app.route('/api')
def api():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')
    
    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })
    return "Item stored successfully!"

if __name__ == '__main__':
    app.run(debug=True)