from fastapi import APIRouter, Response, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import onnxruntime
import numpy as np
from PIL import Image
import io
import os
import base64
from app.core.config import settings

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Check if model exists
if not os.path.exists(settings.onnx_model_path):
    raise FileNotFoundError(f"ONNX model not found at {settings.onnx_model_path}")

# Load the ONNX model
try:
    session = onnxruntime.InferenceSession(settings.onnx_model_path, providers=["CPUExecutionProvider"])
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name
except Exception as e:
    raise RuntimeError(f"Failed to load ONNX model: {str(e)}")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

def generate_single_image():
    # Generate a random latent vector
    random_input = np.random.randn(1, settings.latent_size, 1, 1).astype(np.float32)
    
    # Run inference
    output = session.run([output_name], {input_name: random_input})[0]
    
    # Convert output tensor to image format
    generated_image = (output[0].transpose(1, 2, 0) + 1) * 127.5  # Convert from [-1,1] to [0,255]
    generated_image = np.clip(generated_image, 0, 255).astype(np.uint8)
    
    # Convert NumPy array to PIL Image
    return Image.fromarray(generated_image)

@router.get("/api/generate")
async def generate_image(num_images: int = 4):
    try:
        # Limit the number of images to 4 or 8
        if num_images not in [4, 8]:
            num_images = 4
        
        # Generate multiple images
        images = [generate_single_image() for _ in range(num_images)]
        
        # Get the dimensions of the first image to determine grid size
        img_width, img_height = images[0].size
        
        # Determine grid layout based on number of images
        if num_images == 4:
            grid_size = (2, 2)  # 2x2 grid
        else:  # num_images == 8
            grid_size = (2, 4)  # 2x4 grid
        
        # Create a new image to hold the grid
        grid_width = grid_size[1] * img_width
        grid_height = grid_size[0] * img_height
        grid_img = Image.new('RGB', (grid_width, grid_height))
        
        # Place each image in the grid
        for i, img in enumerate(images):
            row = i // grid_size[1]
            col = i % grid_size[1]
            grid_img.paste(img, (col * img_width, row * img_height))
        
        # Save combined image to memory
        img_bytes = io.BytesIO()
        grid_img.save(img_bytes, format="PNG")
        img_bytes.seek(0)

        # Return combined image as response
        return Response(content=img_bytes.getvalue(), media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image generation failed: {str(e)}")