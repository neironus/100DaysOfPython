from random import randint

SIZE_BOARD = 10
NUMBER_OF_TRY_ALLOWED = 20
NUMBER_BOATS = 5
HIT_SYMBOL = 'X'
MISS_SYMBOL = 'M'

board = []
boats = []

class Boat(object):
    #Create a new boat
    def __init__(self, row, col, direction, size):
        self.row = row
        self.col = col
        self.direction = direction
        self.size = size
        self.count_hit = 0
        pass

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
                if row == self.row and x == self.col:
                    return True
            else:
                return False

    def hit(self):
        self.count_hit += 1

    def sunk(self):
        return self.count_hit == self.size

    def __repr__(self):
        return '[ %d-%d %d %d ]' % (self.row, self.col, self.direction, self.size)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def boat_create(board):
    row = random_row(board)
    col = random_col(board)

    #create a direction 0 = down 1 = right
    direction = randint(0, 1)

    #size of the boat
    size = randint(1,5)

    if boat_possible(row, col, direction, size) and not boat_exist(boats, row, col):
        boats.append(Boat(row, col, direction, size))
    else:
        boat_create(board)


#check if the position is in the board
def boat_possible(row, col, direction, size):
    if direction == 0: #boat going down
        return row + size <= SIZE_BOARD - 1
    else: #boat going right
        return col + size <= SIZE_BOARD -1

#check if a boat exist
def boat_exist(boats, row, col):
    for boat in boats:
        if boat.have_a_part_at(row, col):
            return True
    else:
        return False

def position_already_played(board, row, col):
    return board[row][col] != 'O' #Not hit or miss

for x in range(SIZE_BOARD):
    board.append(["O"] * SIZE_BOARD)


#Create x boats
for i in range(NUMBER_BOATS):
    boat_create(board)

print boats

boats_find = 0
for turn in range(NUMBER_OF_TRY_ALLOWED):
    print "Turn", turn +1
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    # Dont use user input
    # guess_row = random_row(board)
    # guess_col = random_col(board)

    #Is in the ocean ?
    if (guess_row < 0 or guess_row > SIZE_BOARD) or (guess_col < 0 or guess_col > SIZE_BOARD):
        print "Oops, that's not even in the ocean."
    else:
        if position_already_played(board, guess_row, guess_col):
            print "You guessed that one already."
        else:
            for boat in boats:
                if(boat.have_a_part_at(guess_row, guess_col)):
                    boat.hit()
                    print boat
                    if boat.sunk():
                        board[guess_row][guess_col] = HIT_SYMBOL
                        boats_find += 1
                        print "Congratulations! You sunk a battleship!. %d remaining" % int(NUMBER_BOATS - boats_find)
                    else:
                        board[guess_row][guess_col] = HIT_SYMBOL
                        print "Boat hit"
                    break
            else:
                board[guess_row][guess_col] = MISS_SYMBOL
                print "You missed my battleship!"

    print_board(board)
    print " "

    if turn == NUMBER_OF_TRY_ALLOWED-1:
        print "Game Over"

    if NUMBER_BOATS == boats_find:
        print "You won !! GG DUDE!"
        break
