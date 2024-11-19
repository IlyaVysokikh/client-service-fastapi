from fastapi import FastAPI

from src.web.user_handlers import user_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="user service api",
        docs_url="/api/docs",
        description="api for user service",
        debug=True,
    )

    app.include_router(user_router, prefix="/users")

    return app


app = create_app()