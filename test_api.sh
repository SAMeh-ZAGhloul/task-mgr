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
