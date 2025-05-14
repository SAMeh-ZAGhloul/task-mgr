"""
Task Manager Backend Server
--------------------------
A Flask-based REST API that manages tasks for the AI Coding Task Manager.
Provides endpoints for retrieving and updating tasks, with data persistence
using a JSON file.

The server is configured to be accessible over the network, listening on 
all interfaces (0.0.0.0) on port 3000.
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes to allow cross-origin requests

# Data file path for persistent storage
DATA_FILE = 'task-mgr-db.json'

def load_tasks():
    """
    Load tasks from the JSON file.
    Returns an empty list if the file doesn't exist.
    """
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """
    Save tasks to the JSON file.
    Args:
        tasks (list): List of task dictionaries to save
    """
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f)

@app.route('/')
def serve_frontend():
    """Serve the frontend HTML file"""
    return send_file('task-mgr-FE.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    GET endpoint to retrieve all tasks
    Returns:
        JSON response containing list of all tasks
    """
    return jsonify(load_tasks())

@app.route('/tasks', methods=['POST'])
def update_tasks():
    """
    POST endpoint to update tasks
    Expects:
        JSON body containing the complete list of tasks
    Returns:
        JSON response indicating success
    """
    tasks = request.json
    save_tasks(tasks)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    # Start server to listen on all interfaces (0.0.0.0)
    # This makes the server accessible over the network
    app.run(host='0.0.0.0', port=3000)
