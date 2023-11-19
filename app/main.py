from fastapi import FastAPI

from app.config import Settings
from app.routes import router


def get_app() -> FastAPI:
    
    app = FastAPI(**settings.fastapi_kwargs)

    app.include_router(router)

    return app


settings = Settings()
app = get_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
