from pydantic.v1 import BaseSettings


class Configs(BaseSettings):
    PG_CONNECTION_URI: str = "postgresql+asyncpg://myuser:mypassword@postgresql:5432/mydatabase"
    PG_RO_CONNECTION_URI: str = "postgresql+asyncpg://myuser:mypassword@localhost:5432/mydatabase_readonly"

    RABBITMQ_HOST: str = "localhost"
    RABBITMQ_PORT: str = "5672"
    RABBITMQ_USER: str = "auth"
    RABBITMQ_PASS: str = "password"

    class Config:
        env_file = ".env"