"""Welcome To Battleship - this is a classic board game.
                There will be a single ship hidden in a location on a
                5 * 5 grid. The player will have 10 gueses to try to
                sink the ship."""

from random import randint
                                           #First thing is to setup a game board
board = []  

for x in range(0, 5):                      #making a 5 x 5 grid of all "O"s
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
      print " ".join(row)   #to turn the row as "O O O O O"


print_board(board)

def random_row(board):                     #to create rows
  return randint(0, len(board) - 1)

def random_col(board):                     #to create columns
  return randint(0, len(board[0]) - 1)

                                           #Storing the coordinates of the ship in variables
ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col


for turn in range(4):
  print "Turn", turn + 1
 
                                           #to give input as player's guess
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

                                           #checking the player's guess
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"   
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"   #to see if the guessed location already has an 'X' in it.
    if (turn == 3):
      print "Game Over"
    print_board(board)
   
