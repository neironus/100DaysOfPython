import os
import sqlalchemy

from models import ModelBase

__factory = None


def get_db_path(filename: str) -> str:
    """
    Get the db full path

    :param filename: Name of the db
    """

    dir_path = os.path.dirname(__file__)
    return os.path.join(dir_path, filename)


def global_init():
    """
    Init the session
    """
    global __factory

    full_file = get_db_path('guessing.db')
    conn_str = 'sqlite:///' + full_file

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
