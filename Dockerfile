FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create models directory if it doesn't exist
RUN mkdir -p models

# Make sure the model is in the correct location
# You need to add your generator.onnx file to the models directory before building the image
# or use a volume mount when running the container

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]