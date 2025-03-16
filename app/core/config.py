from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Assignment 02 Gen-AI"
    debug: bool = False
    onnx_model_path: str = "models/generator.onnx"
    latent_size: int = 100
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()