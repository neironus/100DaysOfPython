import os
import sqlalchemy
from flask import current_app

from models import ModelBase

__factory = None


def global_init():
    """
    Init the session
    """
    global __factory

    conn_str = 'sqlite://' + current_app.config['DATABASE_URI']

    engine = sqlalchemy.create_engine(conn_str, echo=False)
    ModelBase.metadata.create_all(engine)

    __factory = sqlalchemy.orm.sessionmaker(bind=engine)


def session_factory():
    """
    Get a sqlalchemy session or create if not set

    :return: sqlalchemy session
    """
    global __factory

    if __factory is None:
        global_init()

    return __factory()
