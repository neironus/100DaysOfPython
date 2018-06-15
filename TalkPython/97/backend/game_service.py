import uuid
from collections import OrderedDict
from typing import Optional
from db.db_tools import session_factory
from models import Game, Guess, Player


def get_player(idx: str = None, name: str = None) -> Optional[Player]:
    """
    Get the player if found in db by his name or id

    :param idx: id of player
    :param name: Player name

    :return: Return the player or None if not found
    """
    if not idx and not name:
        raise Exception('No idx or name specified.')

    session = session_factory()

    player = session.query(Player)
    if idx:
        player = player.filter(Player.id == idx)

    if name:
        player = player.filter(Player.name == name)

    player = player.first()
    session.close()

    return player


def find_or_create_player(name: str) -> Player:
    """
    Find or create the player if not found

    :param name: Name of the player

    :return: The player
    """
    player = get_player(name=name)

    if not player:
        player = create_player(name)

    return player


def create_player(name: str) -> Player:
    """
    Create a player
    :param name: Name of the player

    :return: The player
    """

    if not name.strip():
        raise Exception('No value for name')

    player = get_player(name=name)

    if player:
        raise Exception('Player already exist.')

    player = Player(name=name)
    session = session_factory()
    session.add(player)
    session.commit()
    session.close()

    return get_player(name=name)


def save_game(idx: str, id_player: int, answer: int) -> None:
    game = Game(id=idx, id_player=id_player, answer=answer)

    session = session_factory()
    session.add(game)
    session.commit()
    session.close()


def save_guess(guess: int, guess_nb: int, won: bool, id_game: str) -> None:
    guess = Guess(guess=guess, guess_number=guess_nb,
                  is_winning_guess=won, id_game=id_game)

    session = session_factory()
    session.add(guess)
    session.commit()
    session.close()


def get_stats():
    stats = OrderedDict()

    # session = session_factory()
    # players = session.query(Player).order_by(Player.name).all()
    #
    # for player in players:
    #     stats[player.name] = list()
    #
    #     games = session.query(Game).filter(Game.id_player == player.id).all()
    #
    #     for game in games:
    #         final_guess = session.query(Guess).filter(Guess.id_game == game.id) \
    #             .filter(Guess.is_winning_guess == True).first()
    #
    #         if final_guess:
    #             stats[player.name].append(final_guess.guess_number)
    #
    # session.close()

    return stats


def get_game(idx: str) -> Optional[Game]:
    """
    Get a game by his id or name

    :param idx: Id of game

    :return: The game
    """
    session = session_factory()
    game = session.query(Game).filter(Game.id == idx).first()

    session.close()

    return game
