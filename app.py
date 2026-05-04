from pydantic import BaseSettings


class Config(BaseSettings):
    api_key: str = ""
