from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="user service api",
        docs_url="/api/docs",
        description="api for user service",
        debug=True,
    )

    return app
