import sqlalchemy

from models.model_base import ModelBase


class Game(ModelBase):
    __tablename__ = 'games'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True, unique=True)
    answer = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    id_player = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
