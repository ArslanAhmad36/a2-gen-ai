# Assignment-02 Gen-AI Image Generator API

A FastAPI application that generates images using an DCGAN(ONNX model) with a simple web interface.

## Features

- Web interface with a button to generate images
- FastAPI backend for image generation using ONNX Runtime
- Structured project layout
- Docker support for easy deployment

## Prerequisites

- Python 3.9+
- An ONNX generator model

## Installation

### Local Development

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/onnx-image-generator.git
   cd onnx-image-generator
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

4. Place your ONNX model:
   - Put your `generator.onnx` file in the `models/` directory
   - Or update the `onnx_model_path` in `app/core/config.py` to point to your model

5. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

6. Open your browser and navigate to:
   - http://localhost:8000/ - Web interface for generating images
   - http://localhost:8000/api/generate - Direct API endpoint for image generation
   - http://localhost:8000/docs - API documentation

### Using Docker

1. Place your ONNX model in the `models/` directory

2. Build the Docker image:
   ```
   docker build -t onnx-image-generator .
   ```

3. Run the container:
   ```
   docker run -p 8000:8000 onnx-image-generator
   ```

4. Access the web interface at http://localhost:8000

## API Endpoints

- `GET /`: Web interface with a button to generate images
- `GET /api/generate`: Generates and returns a random image

## Model Information

This API uses an ONNX model for image generation. The model should:

- Accept a latent vector input of shape `(1, 100, 1, 1)` (default)
- Output an image tensor
- Be trained to output values in the range [-1, 1]

You can adjust the latent vector size in `app/core/config.py` if your model uses a different dimension.

## Deployment

This application is deployed on KOYEB
