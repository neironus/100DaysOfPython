import logbook
from random import randint

game_log = logbook.Logger('Game')


class Game(object):
    board = []
    boats = []
    boats_finds = 0
    symbol_hit = 'X'
    symbol_miss = 'M'
    turn_current = 1

    # Init a new game
    def __init__(self, board_size, boats_number, turn_max):
        game_log.info('Create new game')
        self.board_size = board_size
        self.boats_number = boats_number
        self.turn_max = turn_max

        self.board = [["O"] * board_size for x in range(board_size)]

        # Create x boats
        for i in range(boats_number):
            self.boat_create()

    def __repr__(self):
        return 'Current turn: {}, Boats finds {}'.format(
            self.turn_current, self.boats_finds)

    @property
    def boat_alive(self):
        return self.boats_number - self.boats_finds

    # Random a row
    def random_row(self):
        return randint(0, len(self.board) - 1)

    # Random a col
    def random_col(self):
        return randint(0, len(self.board[0]) - 1)

    # Print the board
    def board_print(self):
        for row in self.board:
            print(" ".join(row))

    # check if the position is in the board
    def boat_possible(self, row, col, direction, size):
        if direction == 0:  # boat going down
            return row + size <= self.board_size - 1
        else:  # boat going right
            return col + size <= self.board_size - 1

    # check if a boat exist at a coord
    def boat_exist(self, row, col):
        return [boat for boat in self.boats if boat.have_a_part_at(row, col)]

    # create a boat
    def boat_create(self):
        row = self.random_row()
        col = self.random_col()

        # create a direction 0 = down 1 = right
        direction = randint(0, 1)

        # size of the boat
        size = randint(1, 5)

        if (self.boat_possible(row, col, direction, size) and not
                self.boat_exist(row, col)):
            self.boats.append(Boat(row, col, direction, size))
        else:
            self.boat_create()

    # Does the guess is possible ? (In the board)
    def guess_possible(self, row, col):
        return ((row >= 0 and row < self.board_size) and
                (col >= 0 and col < self.board_size))

    # Does the position has already been played ?
    def position_already_played(self, row, col):
        return self.board[row][col] != 'O'  # Still default symbol

    # Play the game
    def play(self):
        while self.turn_current <= self.turn_max:
            self.turn_new()

            if self.game_done():
                game_log.info('Game won with {} turns'.format(self.turn_current))
                print("You won !! GG DUDE!")
                break
        else:
            print("Game Over !!")
            game_log.info("Game lost")

    # New turn
    def turn_new(self):
        print("Turn", self.turn_current)

        try:
            guess_row = int(input("Guess Row: "))
            guess_col = int(input("Guess Col: "))
        except Exception:
            msg = '\n> THE DATA ENTERED IS NOT VALID \n'
            print(msg)
            game_log.error(msg)
            return

        self.turn_current += 1

        # Dont use user input
        # guess_row = random_row(board)
        # guess_col = random_col(board)

        # Is in the ocean ?
        if not self.guess_possible(guess_row, guess_col):
            msg = "Oops, that's not even in the ocean."
            print(msg)
            game_log.error(msg)
        else:
            if self.position_already_played(guess_row, guess_col):
                msg = "You guessed that one already."
                print(msg)
                game_log.error(msg)
            else:
                for boat in self.boats:
                    if(boat.have_a_part_at(guess_row, guess_col)):
                        boat.hit()
                        if boat.sunk():
                            self.board[guess_row][guess_col] = self.symbol_hit
                            self.boats_finds += 1
                            print(
                                "Congratulations! You sunk a battleship!. "
                                "{} remaining".format(self.boat_alive)
                            )
                            game_log.error('Boat sunk {} remaining'.format(self.boat_alive))
                        else:
                            self.board[guess_row][guess_col] = self.symbol_hit
                            msg = "Boat hit"
                            print(msg)
                            game_log.info(msg)
                        break
                else:
                    self.board[guess_row][guess_col] = self.symbol_miss
                    msg = "You missed my battleship!"
                    print(msg)
                    game_log.error(msg)

        self.board_print()
        print(" ")

    # Does the game is done ? (All boats finds)
    def game_done(self):
        return self.boats_number == self.boats_finds


boat_log = logbook.Logger('Boat')

class Boat(object):
    # Create a new boat
    def __init__(self, row, col, direction, size):
        self.row = row
        self.col = col
        self.direction = direction
        self.size = size
        self.count_hit = 0
        pass

    def __repr__(self):
        return '[{}-{} {} {} {}]'.format(
            self.row, self.col, self.direction, self.size, self.count_hit
        )

    # Return if the boat have a part in row/col
    def have_a_part_at(self, row, col):
        if self.direction == 0:  # boat going down
            for y in range(self.row, self.row + self.size):
                if (y == row and col == self.col):
                    return True
        else:  # boat going right
            for x in range(self.col, self.col + self.size):
                if (row == self.row and x == col):
                    return True

        return False

    # The boat has been hit
    def hit(self):
        self.count_hit += 1

    # Is the boat sunk?
    def sunk(self):
        boat_log.info('Boat sunk {}'.format(self))
        return self.count_hit == self.size
