from fastapi import FastAPI
from app.core.config import settings
from app.api.endpoints import router

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

app.include_router(router)

"""if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)"""