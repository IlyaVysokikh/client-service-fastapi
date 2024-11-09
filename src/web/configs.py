from pydantic import BaseModel


class Configs(BaseModel):
    PG_CONNECTION_URI: str
    PG_RO_CONNECTION_URI: str
