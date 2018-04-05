from unittest.mock import patch
import random

from battleship_26 import Game, Boat

def test_guess_possible():
    game = Game(10, 5, 20)
    #Outside the grid
    assert game.guess_possible(-1, -1) == False
    assert game.guess_possible(10, 10) == False
    assert game.guess_possible(0, 25) == False
    #Good
    assert game.guess_possible(4, 6) == True

@patch("builtins.input", side_effect=[0, 0, 1, 1, 1, 0, 2, 0, 3, 0, 4, 0])
def test_sink_boat(inp, capfd):
    game = Game(10, 5, 20)
    game.boats = [
        Boat(0, 0, 0, 5),
        Boat(3, 4, 1, 3),
        Boat(2, 2, 0, 4),
        Boat(7, 8, 1, 2),
        Boat(8, 2, 1, 4)
    ]

    game.turn_new()
    out, _ = capfd.readouterr()
    out = out.rstrip().split('\n')
    assert out[0].rstrip() == 'Turn 1'
    assert out[1] == 'Boat hit'

    game.turn_new()
    out, _ = capfd.readouterr()
    out = out.rstrip().split('\n')
    #Miss
    assert out[1] == 'You missed my battleship!'

    game.turn_new()
    game.turn_new()
    capfd.readouterr()
    game.turn_new()
    out, _= capfd.readouterr()
    out = out.rstrip().split('\n')
    #Good
    assert out[0].rstrip() == 'Turn 5'
    game.turn_new()
    out, _ = capfd.readouterr()
    out = out.rstrip().split('\n')
    #Boat sunk
    assert out[1] == 'Congratulations! You sunk a battleship!. 4 remaining'

@patch("builtins.input", side_effect=[0, 0, 0, 0])
def test_already_guess(inp, capfd):
    game = Game(10, 5, 20)
    game.boats = [
        Boat(0, 0, 0, 5),
        Boat(3, 4, 1, 3),
        Boat(2, 2, 0, 4),
        Boat(7, 8, 1, 2),
        Boat(8, 2, 1, 4)
    ]

    game.turn_new()
    capfd.readouterr()

    game.turn_new()
    out, _ = capfd.readouterr()
    out = out.rstrip().split('\n')
    #Good
    assert out[1] == 'You guessed that one already.'

@patch("builtins.input", side_effect=[0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 1, 0, 2, 0 ,3 ,0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 1, 1])
def test_game_over(inp, capfd):
    game = Game(10, 5, 20)
    game.boats = [
        Boat(0, 0, 0, 5),
        Boat(3, 4, 1, 3),
        Boat(2, 2, 0, 4),
        Boat(7, 8, 1, 2),
        Boat(8, 2, 1, 4)
    ]

    game.play();

    out, _= capfd.readouterr()
    out = out.rstrip().split('\n')
    assert out[-1] == 'Game Over !!'

@patch("builtins.input", side_effect=[0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 7, 7, 8, 8, 2, 2, 3, 2, 4, 2, 5, 2, 3, 4, 3, 5, 3, 6, 8, 2, 8, 3, 8, 4, 8, 5, 7, 8, 7, 9])
def test_win_game(inp, capfd):
    game = Game(10, 5, 20)
    game.boats = [
        Boat(0, 0, 0, 5),
        Boat(3, 4, 1, 3),
        Boat(2, 2, 0, 4),
        Boat(7, 8, 1, 2),
        Boat(8, 2, 1, 4)
    ]

    game.play();

    out, _= capfd.readouterr()
    out = out.rstrip().split('\n')
    assert out[-1] == 'You won !! GG DUDE!'

#TEST BOAT
def test_boat_exist():
    boat = Boat(0, 0, 0, 2) #Boat going down
    #good
    assert boat.have_a_part_at(0, 0) == [True]
    assert boat.have_a_part_at(1, 0) == [True]
    #size is only 2
    assert boat.have_a_part_at(2, 0) == []
    #not the good direction
    assert boat.have_a_part_at(0, 1) == []

def test_boat_hit():
    boat = Boat(0, 0, 0, 2) #Boat going down
    boat.hit()
    #First hit
    assert boat.count_hit == 1
    boat.hit()
    #Second hit
    assert boat.count_hit == 2

def test_boat_sunk():
    boat = Boat(0, 0, 0, 2) #Boat going down
    boat.hit()
    #False only 1hit
    assert boat.sunk() == False
    boat.hit()
    #True 2 hit
    assert boat.sunk() == True

def test_print_boat():
    boat = Boat(0, 0, 0, 2) #Boat going down
    #Correct representation
    assert repr(boat) == "[ 0-0 0 2 0]"
    boat.hit()
    #Correct representation
    assert repr(boat) == "[ 0-0 0 2 1]"
