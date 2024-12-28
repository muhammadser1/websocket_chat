# WebSocket Chat Application

This is a simple WebSocket-based chat application built using FastAPI. The application supports multiple clients connecting in real-time, broadcasting messages to all connected clients.

----------

## Features

-   **Real-Time Messaging**: Supports real-time communication between multiple clients using WebSocket.
    
-   **Unique Client Identification**: Each connected client is assigned a unique ID.
    
-   **Broadcast Functionality**: Messages are broadcast to all connected clients.
    
-   **Modular Design**: The project is organized into modular components for scalability and maintainability.
    

----------


## Requirements

-   Python 3.8+
    
-   FastAPI
    
-   Uvicorn
- WebSockets
## Installation
~~~python
pip install -r requirements.txt
~~~
## Usage
1. **Navigate to the Application Directory**:
~~~python
cd app
~~~
2. **Run the Application**:
~~~python
uvicorn main:app --reload
~~~
3. **Open in Browser**: Open `http://127.0.0.1:8000/` in multiple browser windows or tabs to test the chat.

----
## Project Structure

├── main.py                  # Entry point for the application
├── connection_manager.py    # ConnectionManager class
├── routes/
│   ├── home.py              # Route for serving the HTML page
│   ├── websocket.py         # WebSocket endpoint
└── templates/
    └── index.html           # HTML template for the chat

-----
