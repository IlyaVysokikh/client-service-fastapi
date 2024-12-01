from fastapi import FastAPI
from src.web.user_handlers import user_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="auth service api",
        docs_url="/api/docs",
        description="api for auth service",
        debug=True,
    )

    app.include_router(user_router, prefix="/users")

    return app
