# AI Coding Task Manager

A network-enabled task management system designed for coding projects with AI integration. The system consists of a Python Flask backend and a modern web frontend, allowing task management from any device on the network.

## Features

- 📱 Responsive web interface accessible from any device
- 🔄 Real-time task updates with backend synchronization
- 🎯 Kanban board with drag-and-drop functionality
- 🤖 AI instructions field for each task
- 📅 Due date tracking with visual indicators
- 🎨 Priority levels with color coding
- 🌐 Network-enabled architecture

## Project Structure

```
task-mgr/
├── task-mgr-BE.py    # Flask backend server
├── task-mgr-DB.json  # JSON database file
├── task-mgr-FE.html  # Frontend web interface
└── README.md         # This documentation
```

## Network Setup

### Backend Server
The backend server is configured to be accessible over the network by binding to all network interfaces (`0.0.0.0`). This means it can accept connections from:
- Local machine (`localhost` or `127.0.0.1`)
- Other devices on the same network (using the machine's IP address)
- Remote connections (if properly configured with port forwarding)

### How to Access

1. Start the backend server:
   ```bash
   python3 task-mgr-BE.py
   ```

2. The server will start on port 3000 and be accessible at:
   - Local: `http://localhost:3000`
   - Network: `http://<your-ip-address>:3000`

3. To find your IP address:
   - On macOS/Linux: `ifconfig` or `ip addr`
   - On Windows: `ipconfig`

### Security Considerations

- The server is configured for development use
- For production deployment, consider:
  - Using HTTPS
  - Implementing authentication
  - Adding input validation
  - Using a production-grade web server

## API Endpoints

- `GET /` - Serves the frontend HTML interface
- `GET /tasks` - Retrieves all tasks
- `POST /tasks` - Updates the task list

## Frontend Features

1. Task Management
   - Create, edit, and delete tasks
   - Drag-and-drop between columns
   - Priority levels: Low, Medium, High
   - Due date tracking
   - AI instructions field

2. UI Components
   - Kanban board layout
   - Modal forms for task editing
   - Responsive design
   - Visual indicators for task status

## Data Persistence

Tasks are stored in `task-mgr-DB.json` with the following structure:

```json
[
  {
    "id": "unique-task-id",
    "name": "Task Name",
    "description": "Task Description",
    "aiInstructions": "AI-specific instructions",
    "priority": "Low|Medium|High",
    "assignedTo": "Assignee",
    "dueDate": "YYYY-MM-DD",
    "status": "todo|inprogress|completed"
  }
]
```

## Development

To modify the network configuration:
1. Backend (`task-mgr-BE.py`): Change the host/port in `app.run(host='0.0.0.0', port=3000)`
2. Frontend (`task-mgr-FE.html`): Update the fetch URLs to match your server address
