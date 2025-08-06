# Import necessary modules from FastAPI
from fastapi import FastAPI, HTTPException
# Typing is used for type hints, specifically for a list of strings
from typing import List

# Initialize the FastAPI application
app = FastAPI(
    title="Simpler Messages API with FastAPI",
    description="A very basic API to add and retrieve text messages.",
    version="1.0.0"
)

# This will act as our in-memory database for storing messages.
# It's a simple Python list of strings.
messages_db: List[str] = []

# --- API Endpoints (Path Operations) ---

# GET /messages
# Retrieves all messages.
@app.get(
    "/messages",
    response_model=List[str],  # FastAPI will ensure the response is a list of strings
    summary="Retrieve all messages",
    description="Returns a list of all messages currently stored in the in-memory database."
)
async def get_all_messages():
    """
    Returns a list of all messages.
    """
    return messages_db

# POST /messages
# Adds a new message.
@app.post(
    "/messages",
    status_code=201,  # Set the HTTP status code for successful creation
    summary="Add a new message",
    description="Adds a new text message to the in-memory database."
)
async def add_message(message: str):
    """
    Adds a new message to the list.
    - **message**: The text content of the message to add.
    Returns a confirmation message.
    """
    messages_db.append(message)
    return {"message": "Message added successfully!", "content": message}

# To run this API:
# 1. Save the code as main.py
# 2. Install FastAPI and Uvicorn: pip install "fastapi[all]" uvicorn
# 3. Run from your terminal: uvicorn main:app --reload
# 4. Access the interactive documentation at: http://127.0.0.1:8000/docs
