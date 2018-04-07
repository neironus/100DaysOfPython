from unittest.mock import patch
import pytest, random

from actors import Player, Roll
import program

@pytest.fixture()
def player():
    return Player('John')

@pytest.fixture()
def rolls():
    return program.read_rolls()

@pytest.fixture()
def player1():
    return Player('Player 1')

@pytest.fixture()
def player2():
    return Player('Player 2')

### Player tests ###
def test_player_name(player):
    assert player.name == 'John'

def test_player_points(player):
    #Good
    assert player.points == 0
    player.add_point()
    #Good
    assert player.points == 1
    player.add_point()
    player.add_point()
    #Good
    assert player.points == 3

### Roll tests ###
def test_roll_defeat():
    rock = Roll('rock', ['paper'])
    paper = Roll('paper', ['scissor'])
    scissor = Roll('scissor', ['rock'])

    #Paper beat rock
    assert rock.can_defeat(paper) == False
    #Good
    assert rock.can_defeat(scissor) == True
    #Good
    assert paper.can_defeat(rock) == True

### Program tests ###
def test_add_roll():
    row = {'Human': 'win', 'Gun': 'lose', 'Lightning': 'lose', 'Paper': 'lose', 'Tree': 'win', 'Devil': 'lose', 'Wolf': 'win', 'Water': 'lose', 'Scissors': 'win', 'Fire': 'win', 'Dragon': 'lose', 'Snake': 'win', 'Air': 'lose', 'Rock': 'draw', 'Attacker': 'Rock', 'Sponge': 'win'}
    rock = program.add_roll(row)

    assert rock.name == 'Rock'
    assert rock.defeated_by == ['Air', 'Devil', 'Dragon', 'Gun', 'Lightning', 'Paper', 'Water']


@patch("builtins.input", side_effect=[2323, 'asd', 0])
def test_ask_for_roll(inp, rolls):
    #Not a correct roll
    with pytest.raises(ValueError):
        program.ask_for_roll(rolls)

    #Not a number
    with pytest.raises(ValueError):
        program.ask_for_roll(rolls)

    #Good
    assert rolls[0].name == program.ask_for_roll(rolls).name

@patch("builtins.input", side_effect=['John'])
def test_get_players_name(inp):
    assert program.get_players_name() == 'John'


def test_roll_draw(capfd, player1, player2, rolls):
    capfd.readouterr()
    p1_roll = rolls[0]
    p2_roll = rolls[0]
    program.check_result(p1_roll, p2_roll, player1, player2)

    out,_ = capfd.readouterr()
    out = out.rstrip().split('\n')
    #Good
    assert out[0] == '{} roll: {} - {} roll : {}'.format(player1.name, p1_roll.name, player2.name, p2_roll.name)
    #Good
    assert out[1] == 'Same roll'

def test_roll_win(capfd, player1, player2, rolls):
    capfd.readouterr()
    p1_roll = rolls[0]
    p2_roll = rolls[1]
    program.check_result(p1_roll, p2_roll, player1, player2)

    out,_ = capfd.readouterr()
    out = out.rstrip().split('\n')
    #Good
    assert out[0] == '{} roll: {} - {} roll : {}'.format(player1.name, p1_roll.name, player2.name, p2_roll.name)
    #Good
    assert out[1] == '{} won. He have now {} points'.format(player1.name, player1.points)

def test_roll_lose(capfd, player1, player2, rolls):
    capfd.readouterr()
    p1_roll = rolls[1]
    p2_roll = rolls[0]
    program.check_result(p1_roll, p2_roll, player1, player2)

    out,_ = capfd.readouterr()
    out = out.rstrip().split('\n')
    #Good
    assert out[0] == '{} roll: {} - {} roll : {}'.format(player1.name, p1_roll.name, player2.name, p2_roll.name)
    #Good
    assert out[1] == '{} won. He have now {} points'.format(player2.name, player2.points)
