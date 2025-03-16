from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.core.config import settings
from app.api.generator import router

app = FastAPI(
    title=settings.app_name,
    description="API for generating images using an GAN model",
    version="1.0.0",
    debug=settings.debug
)

app.include_router(router)

"""if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)"""