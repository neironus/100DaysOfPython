from random import randint

SIZE_BOARD = 10
NUMBER_OF_TRY_ALLOWED = 20
NUMBER_BOATS = 1
HIT_SYMBOL = 'X'
MISS_SYMBOL = 'M'

board = []
#boat structure [row, col, direction, size, hit]
boats = []

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

  if boat_possible(row, col, direction, size) and not boat_exist(boats, row, col, direction, size):
    boats.append([row, col, direction, size, 0])
  else:
    boat_create(board)


#check if the position is in the board
def boat_possible(row, col, direction, size):
  if direction == 0: #boat going down
    return row + size <= SIZE_BOARD - 1
  else: #boat going right
    return col + size <= SIZE_BOARD -1

#check if a boat exist
def boat_exist(boats, row, col, direction, size):
  if direction == 0: #boat going down
    for y in range(row, row + size):
      if boat_part_exist(boats, y, col):
        return True
  else: #boat going right
    for x in range(col, col + size):
      if boat_part_exist(boats, row, x):
        return True

  return False


#Check if there is a part of a boat in the position
def boat_part_exist(boats, row, col):
  for boat in boats:
    if(boat[2] == 0): #boat going down
      for y in range(boat[0], boat[0] + boat[3]):
        if(row == y and col == boat[1]):
          return True
    else: #boat going right
      for x in range(boat[1], boat[1] + boat[3]):
        if(row == boat[0] and col == x):
          return True

  return False

#Boat has been hit
def boat_hit(boats, row, col):
  found = False
  for i in range(len(boats)):
    if(boats[i][2] == 0): #boat going down
      for y in range(boats[i][0], boats[i][0] + boats[i][3]):
        if(row == y and col == boats[i][1]):
          found = True
          break
    else: #boat going right
      for x in range(boats[i][1], boats[i][1] + boats[i][3]):
        if(row == boats[i][0] and col == x):
          found = True
          break

    if found:
      boats[i][4] += 1
      if boats[i][3] == boats[i][4]:
        boats.pop(i)
        return 10
      else:
        return 20
      break

def position_already_played(board, row, col):
  return board[row][col] == HIT_SYMBOL or board[row][col] == MISS_SYMBOL

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
    elif boat_part_exist(boats, guess_row, guess_col):
      type = boat_hit(boats, guess_row, guess_col)

      if(type == 10): #sunk
        board[guess_row][guess_col] = HIT_SYMBOL
        boats_find += 1
        print "Congratulations! You sunk a battleship!. %d remaining" % int(NUMBER_BOATS - boats_find)
      else: #hit
        board[guess_row][guess_col] = HIT_SYMBOL
        print "Boat hit"
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
