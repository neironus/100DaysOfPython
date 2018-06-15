from collections import OrderedDict
from typing import Optional

from data import session_factory
from models.player import Player
from models.game import Game
from models.guess import Guess


def get_player(name: str) -> Optional[Player]:
    session = session_factory.create_session()

    player = session.query(Player).filter(Player.name == name).first()

    session.close()

    return player


def find_or_create_player(name: str) -> Player:
    player = get_player(name)

    if player:
        return player

    player = Player(name=name)
    session = session_factory.create_session()
    session.add(player)
    session.commit()
    session.close()

    return get_player(name)


def save_game(idx: str, id_player: int, answer: int) -> None:
    game = Game(id=idx, id_player=id_player, answer=answer)

    session = session_factory.create_session()
    session.add(game)
    session.commit()
    session.close()


def save_guess(guess: int, guess_nb: int, won: bool, id_game: str) -> None:
    guess = Guess(guess=guess, guess_number=guess_nb,
                  is_winning_guess=won, id_game=id_game)

    session = session_factory.create_session()
    session.add(guess)
    session.commit()
    session.close()


def get_stats():
    session = session_factory.create_session()

    stats = OrderedDict()

    players = session.query(Player).order_by(Player.name).all()

    for player in players:
        stats[player.name] = list()

        games = session.query(Game).filter(Game.id_player == player.id).all()

        for game in games:
            final_guess = session.query(Guess).filter(Guess.id_game == game.id)\
                .filter(Guess.is_winning_guess == True).first()

            if final_guess:
                stats[player.name].append(final_guess.guess_number)

    session.close()

    return stats



