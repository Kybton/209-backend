from sqlalchemy.ext.declarative import declarative_base
from configs.Database import Engine

EntityMeta = declarative_base()


def init():
    print("init has been called")
    EntityMeta.metadata.create_all(Engine)
