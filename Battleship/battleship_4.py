from random import randint

SIZE_BOARD = 10
NUMBER_OF_TRY_ALLOWED = 10
NUMBER_BOATS = 10
HIT_SYMBOL = 'X'
MISS_SYMBOL = 'M'

board = []
boats = []

def print_board(board):
  for row in board:
    print " ".join(row)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

def create_boat(board):
  row = random_row(board)
  col = random_col(board)

  if boat_exist(boats, row, col):
    create_boat(board)
  else:
    boats.append([row, col])

  print boats

#Check if there is a boat in the position
def boat_exist(boats, row, col):
  for boat in boats:
    if boat[0] == row and boat[1] == col:
      return True

  return False

#Remove a boat by his position
def remove_boat(boats, row, col):
  boats.remove([row, col])

def position_already_played(board, row, col):
  return board[row][col] == HIT_SYMBOL or board[row][col] == MISS_SYMBOL

for x in range(SIZE_BOARD):
  board.append(["O"] * SIZE_BOARD)


#Create x boats
for i in range(NUMBER_BOATS):
  create_boat(board)

boats_find = 0
for turn in range(NUMBER_OF_TRY_ALLOWED):
  print "Turn", turn +1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  # Dont use user input
  # guess_row = random_row(board)
  # guess_col = random_col(board)

  if boat_exist(boats, guess_row, guess_col):
    boats_find += 1
    remove_boat(boats, guess_row, guess_col)
    board[guess_row][guess_col] = HIT_SYMBOL
    print "Congratulations! You sunk a battleship!. %d remaining" % int(NUMBER_BOATS - boats_find)
  else:
    if (guess_row < 0 or guess_row > SIZE_BOARD) or (guess_col < 0 or guess_col > SIZE_BOARD):
      print "Oops, that's not even in the ocean."
    elif position_already_played(board, guess_row, guess_col):
      print "You guessed that one already."
    else:
      board[guess_row][guess_col] = MISS_SYMBOL
      print "You missed my battleship!"

    print_board(board)
    print " "

    if turn == NUMBER_OF_TRY_ALLOWED-1:
        print "Game Over"
