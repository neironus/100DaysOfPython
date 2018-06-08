import sqlalchemy

from models.model_base import ModelBase


class Guess(ModelBase):
    __tablename__ = 'guesses'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    guess = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    guess_number = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    is_winning_guess = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    id_game = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
