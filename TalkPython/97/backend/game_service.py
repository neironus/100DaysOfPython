import random
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


def create_game(id_game: str, id_player: int) -> None:
    """
    Create a game with his id and id_player specified

    :param id_game: The id of the game
    :param id_player: The id of the player playing this game
    """
    game = Game(id=id_game, answer=random.randint(1, 100), id_player=id_player)

    session = session_factory()
    session.add(game)
    session.commit()
    session.close()


def is_winning_guess(id_game: str, guess: int) -> bool:
    """
    Check if the guess if the answer for this game

    :param id_game: Id of the game
    :param guess: The player guess

    :return: True if it's the answer False otherwise
    """
    session = session_factory()

    game = session.query(Game).filter(Game.id == id_game).first()

    return game.answer == guess


def save_guess(guess: int, id_game: str, id_player: int) -> None:
    """
    Save the user guess
    :param guess: The guess
    :param id_game: The id of the game
    :param id_player: The id of the player
    """
    session = session_factory()

    game = session.query(Game).filter(Game.id == id_game).first()
    if not game:
        create_game(id_game, id_player)

    last_guess = get_last_guess_of_game(id_game)
    if not last_guess:
        guess_count = 1
    else:
        guess_count = last_guess.guess_count + 1

    won = is_winning_guess(id_game, guess)

    guess = Guess(guess=guess, guess_count=guess_count,
                  is_winning_guess=won, id_game=id_game)

    session.add(guess)
    session.commit()
    session.close()


def get_last_guess_of_game(id_game: str) -> Guess:
    """
    Get the last guess of the game specified

    :param id_game: The id of the game

    :return: The guess
    """
    session = session_factory()

    guess = session.query(Guess).filter(Guess.id_game == id_game) \
        .order_by(Guess.id.desc()).first()

    session.close()

    return guess


def get_status_last_guess(id_game: str) -> int:
    """
    Ge the status for the last guess, if the guess was lower/higher/same of the
    answer

    :param id_game: Id of the game

    :return: 0 for lower, 1 for correct, 2 for higher
    """
    game = get_game(id_game)
    guess = get_last_guess_of_game(id_game)

    if guess.guess < game.answer:
        return 0
    elif guess.is_winning_guess:
        return 1
    else:
        return 2


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
