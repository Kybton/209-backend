from toml import load as toml_load
from pydantic_settings import BaseSettings


class EnvironmentSettings(BaseSettings):
    DATABASE_DIALECT: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str

    def __init__(self):
        env = toml_load("./configs/configs.toml")
        self.DATABASE_DIALECT = env["database"]["dialect"]
        self.DATABASE_HOST = env["database"]["host"]
        self.DATABASE_PORT = env["database"]["port"]
        self.DATABASE_NAME = env["database"]["database"]
        self.DATABASE_USERNAME = env["database"]["username"]
        self.DATABASE_PASSWORD = env["database"]["password"]


def get_environment_variables():
    return EnvironmentSettings()
