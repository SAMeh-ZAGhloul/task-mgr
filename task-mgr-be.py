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
from flasgger import Swagger, swag_from
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes to allow cross-origin requests

# Configure Swagger
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs"
}

swagger_template = {
    "info": {
        "title": "Task Manager API",
        "description": "API for managing tasks in the AI Coding Task Manager",
        "contact": {
            "responsibleDeveloper": "Developer",
            "email": "developer@example.com"
        },
        "version": "1.0"
    },
    "schemes": [
        "http",
        "https"
    ]
}

swagger = Swagger(app, config=swagger_config, template=swagger_template)

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
@swag_from({
    'responses': {
        200: {
            'description': 'List of tasks',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'string', 'description': 'Unique task identifier'},
                        'name': {'type': 'string', 'description': 'Task name'},
                        'description': {'type': 'string', 'description': 'Task description'},
                        'aiInstructions': {'type': 'string', 'description': 'AI-specific instructions'},
                        'priority': {'type': 'string', 'enum': ['Low', 'Medium', 'High'], 'description': 'Task priority'},
                        'assignedTo': {'type': 'string', 'description': 'Task assignee'},
                        'dueDate': {'type': 'string', 'format': 'date', 'description': 'Task due date'},
                        'status': {'type': 'string', 'enum': ['todo', 'inprogress', 'completed'], 'description': 'Task status'}
                    }
                }
            }
        }
    }
})
def get_tasks():
    """
    Get all tasks
    ---
    tags:
      - tasks
    responses:
      200:
        description: List of all tasks
    """
    return jsonify(load_tasks())

@app.route('/tasks', methods=['POST'])
@swag_from({
    'parameters': [{
        'in': 'body',
        'name': 'body',
        'required': True,
        'schema': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique task identifier'},
                    'name': {'type': 'string', 'description': 'Task name'},
                    'description': {'type': 'string', 'description': 'Task description'},
                    'aiInstructions': {'type': 'string', 'description': 'AI-specific instructions'},
                    'priority': {'type': 'string', 'enum': ['Low', 'Medium', 'High'], 'description': 'Task priority'},
                    'assignedTo': {'type': 'string', 'description': 'Task assignee'},
                    'dueDate': {'type': 'string', 'format': 'date', 'description': 'Task due date'},
                    'status': {'type': 'string', 'enum': ['todo', 'inprogress', 'completed'], 'description': 'Task status'}
                },
                'required': ['id', 'name', 'status']
            }
        }
    }],
    'responses': {
        200: {
            'description': 'Tasks updated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {'type': 'string', 'example': 'success'}
                }
            }
        }
    }
})
def update_tasks():
    """
    Update tasks
    ---
    tags:
      - tasks
    parameters:
      - in: body
        name: tasks
        description: List of tasks to update
        required: true
        schema:
          type: array
          items:
            $ref: '#/definitions/Task'
    responses:
      200:
        description: Tasks updated successfully
    definitions:
      Task:
        type: object
        properties:
          id:
            type: string
            description: Unique task identifier
          name:
            type: string
            description: Task name
          description:
            type: string
            description: Task description
          aiInstructions:
            type: string
            description: AI-specific instructions
          priority:
            type: string
            enum: [Low, Medium, High]
            description: Task priority
          assignedTo:
            type: string
            description: Task assignee
          dueDate:
            type: string
            format: date
            description: Task due date
          status:
            type: string
            enum: [todo, inprogress, completed]
            description: Task status
        required:
          - id
          - name
          - status
    """
    tasks = request.json
    save_tasks(tasks)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    # Start server to listen on all interfaces (0.0.0.0)
    # This makes the server accessible over the network
    app.run(host='0.0.0.0', port=3000)
