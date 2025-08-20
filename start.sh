#!/bin/bash

echo "Starting backend..."
cd backend
uvicorn main:app --reload &
BACKEND_PID=$!
cd ..

# echo "Starting Electron frontend..."
# cd frontend
# npx electron .

echo "Stopping backend..."
kill $BACKEND_PID