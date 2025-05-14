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

## Testing with Postman

You can test the Task Manager APIs using the Postman extension in VS Code or the Postman desktop application.

### Setup in VS Code

1. Install the "Postman" extension from the VS Code marketplace
2. Create a new collection for Task Manager
3. Set the base URL: `http://localhost:3000` or `http://<your-ip-address>:3000`

### Testing Endpoints

1. **GET /tasks**
   ```http
   GET http://localhost:3000/tasks
   ```
   - No request body needed
   - Returns: Array of task objects

2. **POST /tasks**
   ```http
   POST http://localhost:3000/tasks
   Content-Type: application/json

   [
     {
       "id": "task-1",
       "name": "Example Task",
       "description": "Task description",
       "aiInstructions": "AI instructions here",
       "priority": "Medium",
       "assignedTo": "AI",
       "dueDate": "2025-05-14",
       "status": "todo"
     }
   ]
   ```

### Example Requests

1. **Create/Update Tasks**
   ```http
   POST http://localhost:3000/tasks
   Content-Type: application/json

   [
     {
       "id": "task-1",
       "name": "Implement Login",
       "description": "Add user authentication",
       "priority": "High",
       "assignedTo": "Developer",
       "dueDate": "2025-05-20",
       "status": "todo"
     },
     {
       "id": "task-2",
       "name": "Design Dashboard",
       "description": "Create UI mockups",
       "priority": "Medium",
       "assignedTo": "Designer",
       "dueDate": "2025-05-25",
       "status": "inprogress"
     }
   ]
   ```

2. **Retrieve Tasks**
   - Send GET request to `/tasks`
   - Verify the response matches the Task Schema
   - Check status codes and response times

### Testing Tips

1. **Environment Variables**
   - Create environments for different settings (local, network)
   - Set variables like:
     ```json
     {
       "baseUrl": "http://localhost:3000",
       "networkUrl": "http://<your-ip-address>:3000"
     }
     ```

2. **Response Validation**
   - Check response status (200 OK)
   - Validate JSON schema
   - Verify data persistence by:
     1. GET tasks
     2. POST new tasks
     3. GET tasks again to confirm changes

3. **Error Testing**
   - Try invalid task properties
   - Test missing required fields
   - Verify error responses

4. **Collection Runner**
   - Create test sequences
   - Run multiple requests in order
   - Automate testing workflow

## Testing with cURL

You can test the Task Manager APIs directly from the terminal using cURL commands.

### Basic Tests

1. **Get All Tasks**
   ```zsh
   # Simple GET request
   curl http://localhost:3000/tasks

   # GET request with formatted JSON output
   curl http://localhost:3000/tasks | python3 -m json.tool

   # GET request with headers
   curl -v http://localhost:3000/tasks
   ```

2. **Create/Update Tasks**
   ```zsh
   # Create a single task
   curl -X POST http://localhost:3000/tasks \
     -H "Content-Type: application/json" \
     -d '[{
       "id": "task-1",
       "name": "Test Task",
       "description": "Testing with curl",
       "priority": "Medium",
       "assignedTo": "Tester",
       "dueDate": "2025-05-14",
       "status": "todo"
     }]'

   # Create multiple tasks
   curl -X POST http://localhost:3000/tasks \
     -H "Content-Type: application/json" \
     -d '[
       {
         "id": "task-1",
         "name": "First Task",
         "priority": "High",
         "status": "todo"
       },
       {
         "id": "task-2",
         "name": "Second Task",
         "priority": "Medium",
         "status": "inprogress"
       }
     ]'

   # Update tasks with pretty-printed response
   curl -X POST http://localhost:3000/tasks \
     -H "Content-Type: application/json" \
     -d '[{"id": "task-1", "name": "Updated Task", "status": "completed"}]' \
     | python3 -m json.tool
   ```

### Advanced curl Commands

1. **Save Response to File**
   ```zsh
   # Save tasks to JSON file
   curl http://localhost:3000/tasks > tasks_backup.json

   # Save with timestamp
   curl http://localhost:3000/tasks > "tasks_$(date +%Y%m%d_%H%M%S).json"
   ```

2. **Load Tasks from File**
   ```zsh
   # Update tasks from JSON file
   curl -X POST http://localhost:3000/tasks \
     -H "Content-Type: application/json" \
     -d @tasks_backup.json
   ```

3. **Test Network Access**
   ```zsh
   # Get your IP address
   IP=$(ipconfig getifaddr en0)
   
   # Test network access
   curl http://$IP:3000/tasks
   ```

4. **Debug Requests**
   ```zsh
   # Show request headers
   curl -v http://localhost:3000/tasks

   # Show timing information
   curl -w "\nTime: %{time_total}s\n" http://localhost:3000/tasks

   # Test CORS headers
   curl -H "Origin: http://localhost:8000" \
     -v http://localhost:3000/tasks
   ```

5. **Error Testing**
   ```zsh
   # Test invalid content type
   curl -X POST http://localhost:3000/tasks \
     -H "Content-Type: text/plain" \
     -d "invalid data"

   # Test missing required fields
   curl -X POST http://localhost:3000/tasks \
     -H "Content-Type: application/json" \
     -d '[{"description": "Missing required fields"}]'

   # Test invalid JSON
   curl -X POST http://localhost:3000/tasks \
     -H "Content-Type: application/json" \
     -d '{invalid json}'
   ```

6. **One-liner Task Creation**
   ```zsh
   # Quick task creation
   curl -X POST http://localhost:3000/tasks -H "Content-Type: application/json" -d '[{"id":"quick-task-'$(date +%s)'","name":"Quick Task","status":"todo"}]'
   ```

### Shell Script for Automated Testing

Create a file `test_api.sh`:
```bash
#!/bin/bash

# Configuration
BASE_URL="http://localhost:3000"
BOLD="\033[1m"
GREEN="\033[0;32m"
RED="\033[0;31m"
NC="\033[0m" # No Color

echo "${BOLD}Running API Tests${NC}"

# Test 1: Get all tasks (should return empty array or existing tasks)
echo "\n${BOLD}Test 1: GET /tasks${NC}"
GET_RESPONSE=$(curl -s -w "\n%{http_code}" $BASE_URL/tasks)
HTTP_CODE=$(echo "$GET_RESPONSE" | tail -n1)
RESPONSE_BODY=$(echo "$GET_RESPONSE" | sed '$d')

if [ $HTTP_CODE -eq 200 ]; then
    echo "${GREEN}✓ GET /tasks successful${NC}"
    echo "Response: $RESPONSE_BODY"
else
    echo "${RED}✗ GET /tasks failed with code $HTTP_CODE${NC}"
fi

# Test 2: Create new task
echo "\n${BOLD}Test 2: POST /tasks${NC}"
POST_RESPONSE=$(curl -s -w "\n%{http_code}" -X POST \
  -H "Content-Type: application/json" \
  -d '[{
    "id": "test-'"$(date +%s)"'",
    "name": "Curl Test Task",
    "description": "Created by curl test script",
    "priority": "Medium",
    "assignedTo": "Tester",
    "dueDate": "2025-05-14",
    "status": "todo"
  }]' \
  $BASE_URL/tasks)

HTTP_CODE=$(echo "$POST_RESPONSE" | tail -n1)
RESPONSE_BODY=$(echo "$POST_RESPONSE" | sed '$d')

if [ $HTTP_CODE -eq 200 ]; then
    echo "${GREEN}✓ POST /tasks successful${NC}"
    echo "Response: $RESPONSE_BODY"
else
    echo "${RED}✗ POST /tasks failed with code $HTTP_CODE${NC}"
fi

# Test 3: Verify task was created
echo "\n${BOLD}Test 3: Verify task creation${NC}"
GET_RESPONSE=$(curl -s -w "\n%{http_code}" $BASE_URL/tasks)
HTTP_CODE=$(echo "$GET_RESPONSE" | tail -n1)
RESPONSE_BODY=$(echo "$GET_RESPONSE" | sed '$d')

if [ $HTTP_CODE -eq 200 ] && echo "$RESPONSE_BODY" | grep -q "Curl Test Task"; then
    echo "${GREEN}✓ Task verification successful${NC}"
else
    echo "${RED}✗ Task verification failed${NC}"
fi
```

### Running the Tests

1. Make the script executable and run it:
   ```bash
   chmod +x test_api.sh
   ./test_api.sh
   ```

2. Expected output:
   ```
   Running API Tests

   Test 1: GET /tasks
   ✓ GET /tasks successful
   Response: [...]

   Test 2: POST /tasks
   ✓ POST /tasks successful
   Response: {"status":"success"}

   Test 3: Verify task creation
   ✓ Task verification successful
   ```

### Error Testing with cURL

1. **Test Missing Required Fields**
   ```bash
   curl -X POST http://localhost:3000/tasks \
     -H "Content-Type: application/json" \
     -d '[{"description": "Missing required fields"}]'
   ```

2. **Test Invalid Priority**
   ```bash
   curl -X POST http://localhost:3000/tasks \
     -H "Content-Type: application/json" \
     -d '[{
       "id": "task-error",
       "name": "Test Task",
       "priority": "INVALID",
       "status": "todo"
     }]'
   ```

3. **Test Invalid Date Format**
   ```bash
   curl -X POST http://localhost:3000/tasks \
     -H "Content-Type: application/json" \
     -d '[{
       "id": "task-error",
       "name": "Test Task",
       "priority": "Medium",
       "status": "todo",
       "dueDate": "invalid-date"
     }]'
   ```

### Running Tests on macOS/zsh

1. **Make the test script executable**
   ```zsh
   chmod +x test_api.sh
   ```

2. **Start the Flask backend in one terminal**
   ```zsh
   python3 task-mgr-BE.py
   ```

3. **Run the test script in another terminal**
   ```zsh
   ./test_api.sh
   ```

The script will output colored results for each test:
- ✓ Green checkmarks for successful tests
- ✗ Red X's for failed tests

### Test Script Features

- Uses zsh-compatible syntax
- Colored output for better visibility
- HTTP response code validation
- Response body verification
- Automatic test task generation with timestamp-based IDs
- Test sequence with verification steps

### Common Issues on macOS

1. **Script Permission Denied**
   ```zsh
   # Fix with
   chmod +x test_api.sh
   ```

2. **Python Version**
   ```zsh
   # Check Python version
   python3 --version
   
   # If needed, install Python 3
   brew install python3
   ```

3. **Running Multiple Services**
   - Use separate terminal windows/tabs for:
     - Flask backend (port 3000)
     - Django frontend (port 8000)
     - Test script

4. **Finding Your IP Address**
   ```zsh
   # For network testing
   ipconfig getifaddr en0  # For Wi-Fi
   ipconfig getifaddr en1  # For Ethernet
   ```

