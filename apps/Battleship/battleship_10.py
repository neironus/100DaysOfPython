from random import randint

class Game(object):
    board = []
    boats = []
    boats_finds = 0
    symbol_hit = 'X'
    symbol_miss = 'M'
    turn_current = 1

    #Init a new game
    def __init__(self, board_size, boats_number, turn_max):
        self.board_size = board_size
        self.boats_number = boats_number
        self.turn_max = turn_max

        for x in range(board_size):
            self.board.append(["O"] * board_size)

        #Create x boats
        for i in range(boats_number):
            self.boat_create()

    def __repr__(self):
        return 'Current turn: %d, Boats finds %d' % (self.turn_current, self.boats_finds)

    #Random a row
    def random_row(self):
        return randint(0, len(self.board) - 1)

    #Random a col
    def random_col(self):
        return randint(0, len(self.board[0]) - 1)

    #Print the board
    def board_print(self):
        for row in self.board:
            print " ".join(row)

    #check if the position is in the board
    def boat_possible(self, row, col, direction, size):
        if direction == 0: #boat going down
            return row + size <= self.board_size - 1
        else: #boat going right
            return col + size <= self.board_size -1

    #check if a boat exist at a coord
    def boat_exist(self, row, col):
        for boat in self.boats:
            if boat.have_a_part_at(row, col):
                return True
        else:
            return False

    #create a boat
    def boat_create(self):
        row = self.random_row()
        col = self.random_col()

        #create a direction 0 = down 1 = right
        direction = randint(0, 1)

        #size of the boat
        size = randint(1,5)

        if self.boat_possible(row, col, direction, size) and not self.boat_exist(row, col):
            self.boats.append(Boat(row, col, direction, size))
        else:
            self.boat_create()

    #Does the guess is possible ? (In the board)
    def guess_possible(self, row, col):
        return (row >= 0 and row < self.board_size) and (col >= 0 and col < self.board_size)

    #Does the position has already been played ?
    def position_already_played(self, row, col):
        return self.board[row][col] != 'O' #Not hit or miss

    #Play the game
    def play(self):
        while self.turn_current <= self.turn_max:
            game.turn_new()
            self.turn_current += 1

            if game.game_done():
                print "You won !! GG DUDE!"
                break
        else:
            print "Game Over !!"

    #New turn
    def turn_new(self):
        print "Turn", self.turn_current
        guess_row = int(raw_input("Guess Row: "))
        guess_col = int(raw_input("Guess Col: "))

        # Dont use user input
        # guess_row = random_row(board)
        # guess_col = random_col(board)

        #Is in the ocean ?
        if not self.guess_possible(guess_row, guess_col):
            print "Oops, that's not even in the ocean."
        else:
            if self.position_already_played(guess_row, guess_col):
                print "You guessed that one already."
            else:
                for boat in self.boats:
                    if(boat.have_a_part_at(guess_row, guess_col)):
                        boat.hit()
                        if boat.sunk():
                            self.board[guess_row][guess_col] = self.symbol_hit
                            self.boats_finds += 1
                            print "Congratulations! You sunk a battleship!. %d remaining" % int(self.boats_number - self.boats_finds)
                        else:
                            self.board[guess_row][guess_col] = self.symbol_hit
                            print "Boat hit"
                        break
                else:
                    self.board[guess_row][guess_col] = self.symbol_miss
                    print "You missed my battleship!"

        self.board_print()
        print " "

    #Does the game is done ? (All boats finds)
    def game_done(self):
        return self.boats_number == self.boats_finds


class Boat(object):
    #Create a new boat
    def __init__(self, row, col, direction, size):
        self.row = row
        self.col = col
        self.direction = direction
        self.size = size
        self.count_hit = 0
        pass

    def __repr__(self):
        return '[ %d-%d %d %d %d]' % (self.row, self.col, self.direction, self.size, self.count_hit)

    #Display a part of the boat is a the coord
    def have_a_part_at(self, row, col):
        if self.direction == 0: #boat going down
            for y in range(self.row, self.row + self.size):
                if y == row and col == self.col:
                    return True
            else:
                return False
        else: #boat going right
            for x in range(self.col, self.col + self.size):
                if row == self.row and x == col:
                    return True
            else:
                return False

    #The boat has been hit
    def hit(self):
        self.count_hit += 1

    #Is the boat sunk?
    def sunk(self):
        return self.count_hit == self.size

if __name__ == '__main__':
    game = Game(10, 5, 20)
    game.play()
