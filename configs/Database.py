from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from toml import load as toml_load

env = toml_load("./configs/configs.toml")["database"]
DATABASE_URL = f"{env['dialect']}://{env['username']}:{env['password']}@{env['host']}:{env['port']}/{env['database']}"

Engine = create_engine(
    DATABASE_URL,
    future=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=Engine,
    expire_on_commit=False
)


def get_db_connection():
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.remove()
