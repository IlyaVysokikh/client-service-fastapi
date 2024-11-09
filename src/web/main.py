from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="client service api",
        docs_url="/api/docs",
        description="api for client service",
        debug=True,
    )

    return app
