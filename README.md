# AI Coding Task Manager

A network-enabled task management system designed for coding projects with AI integration. The system features a Python Flask backend and two alternative frontends (Static HTML and Django), allowing task management from any device on the network.

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
├── task-mgr-BE.py        # Flask backend server
├── task-mgr-DB.json      # JSON database file
├── task-mgr-FE.html      # Static HTML frontend
├── django-frontend/      # Django-based frontend
│   ├── manage.py         # Django management script
│   ├── taskmgr/         # Django project settings
│   └── tasks/           # Django tasks app
└── README.md            # This documentation
```

## Network Setup

### Backend Server (Flask)
The backend server is configured to be accessible over the network by binding to all network interfaces (`0.0.0.0`). This means it can accept connections from:
- Local machine (`localhost` or `127.0.0.1`)
- Other devices on the same network (using the machine's IP address)
- Remote connections (if properly configured with port forwarding)

The Flask backend runs on port 3000 and serves both frontends.

### Frontend Options

1. **Static HTML Frontend** (Port 3000)
   - Served directly by Flask backend
   - Access via:
     - Local: `http://localhost:3000`
     - Network: `http://<your-ip-address>:3000`
   - Lightweight and simple to deploy
   - Single page application

2. **Django Frontend** (Port 8000)
   - Runs as a separate server
   - Access via:
     - Local: `http://localhost:8000`
     - Network: `http://<your-ip-address>:8000`
   - Full-featured web framework
   - Server-side rendering

### Starting the Services

1. Start the Flask backend:
   ```bash
   python3 task-mgr-BE.py
   ```

2. For Django frontend (optional):
   ```bash
   cd django-frontend
   python3 manage.py runserver 0.0.0.0:8000
   ```

3. To find your IP address:
   - On macOS/Linux: `ifconfig` or `ip addr`
   - On Windows: `ipconfig`

## Frontend Comparison

### Static HTML Frontend
Advantages:
- Simple deployment (served by Flask)
- No additional server required
- Lightweight and fast
- Client-side rendering
- Modern reactive UI

Limitations:
- Limited server-side functionality
- Basic error handling
- No built-in authentication

### Django Frontend
Advantages:
- Robust server-side rendering
- Better error handling and user feedback
- Built-in security features
- Easy to add authentication
- Template inheritance
- Form validation
- Session management

Limitations:
- Requires separate server
- More complex deployment
- Additional resource usage

## Alternative Frontend Frameworks

You can build additional frontends using these popular frameworks:

1. **React.js**
   - Popular choice for single-page applications
   - Rich ecosystem of components
   - Great for complex UIs

2. **Vue.js**
   - Progressive framework
   - Easy learning curve
   - Good for both small and large applications

3. **Angular**
   - Full-featured framework
   - Strong typing with TypeScript
   - Good for large enterprise applications

4. **Svelte**
   - Compile-time framework
   - Very lightweight
   - Great performance

5. **Next.js**
   - React-based with SSR
   - Great for SEO
   - Hybrid static & server rendering

To implement a new frontend:
1. Use the Flask backend API endpoints
2. Configure CORS on the backend (already done)
3. Update the API URLs to point to your Flask backend
4. Implement the task management interface

## Security Considerations

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

## API Documentation

The backend server includes Swagger/OpenAPI documentation using Flasgger. You can access the interactive API documentation at:
- Local: `http://localhost:3000/docs`
- Network: `http://<your-ip-address>:3000/docs`

The Swagger UI provides:
- Interactive API testing
- Detailed endpoint documentation
- Request/response schemas
- Data validation rules
- Example requests and responses

### Available Endpoints

1. `GET /` 
   - Serves the static HTML frontend interface
   - Content-Type: text/html

2. `GET /tasks`
   - Retrieves all tasks
   - Response: Array of task objects
   - Schema validation for response data

3. `POST /tasks`
   - Updates the task list
   - Request Body: Array of task objects
   - Required fields: id, name, status
   - Validates task properties:
     - priority: [Low, Medium, High]
     - status: [todo, inprogress, completed]
     - dueDate: YYYY-MM-DD format

### Task Schema

```json
{
  "id": "string",         // Unique task identifier
  "name": "string",       // Task name
  "description": "string", // Optional task description
  "aiInstructions": "string", // Optional AI-specific instructions
  "priority": "enum",     // Low, Medium, High
  "assignedTo": "string", // Task assignee
  "dueDate": "date",     // YYYY-MM-DD format
  "status": "enum"       // todo, inprogress, completed
}
```

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

