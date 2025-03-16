# Simple FastAPI Application

A simple, production-ready FastAPI application with a clean structure.

## Features

- FastAPI framework with automatic API documentation
- Structured project layout
- Docker support for easy deployment
- Environment variable configuration

## Installation

### Local Development

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fastapi-simple-app.git
   cd fastapi-simple-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

5. Open your browser and navigate to http://localhost:8000/docs to see the API documentation.

### Using Docker

1. Build the Docker image:
   ```
   docker build -t fastapi-simple-app .
   ```

2. Run the container:
   ```
   docker run -p 8000:8000 fastapi-simple-app
   ```

3. Access the API at http://localhost:8000

## API Endpoints

- `GET /`: Returns a hello world message
- `GET /items/{item_id}`: Returns an item by ID with an optional query parameter

## Deployment

This application can be deployed to various platforms:

### KOYEB
