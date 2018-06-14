import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


ModelBase = declarative_base()


class Game(ModelBase):
    __tablename__ = 'games'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True, unique=True)
    answer = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    id_player = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    guesses = relationship('Guess', back_populates='game')

    @property
    def is_done(self):
        print(self.guesses)
        return True

    def to_web(self):
        """
        Transform the data for web exploitation

        :return: The datas transformed
        """
        return {
            'id': self.id,
            'id_player': self.id_player,
            'done': self.is_done
        }


class Guess(ModelBase):
    __tablename__ = 'guesses'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    guess = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    guess_number = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    is_winning_guess = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    id_game = sqlalchemy.Column(sqlalchemy.String,
                                sqlalchemy.ForeignKey('games.id'))

    game = relationship('Game', back_populates="guesses")


class Player(ModelBase):
    __tablename__ = 'players'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)

    def to_web(self):
        """
        Transform the data for web exploitation

        :return: The datas transformed
        """
        return {
            'id': self.id,
            'name': self.name
        }
