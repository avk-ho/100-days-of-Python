# https://www.udemy.com/course/100-days-of-code/learn/practice/1251144/introduction#overview

# Tic Tac Toe

### Notes ###
# 2 players
# Add AI ?
# UI with mouse instead of console and keyboard
# for the grid, use numbers ? coordinates ?

# about the victory conditions
# check for the coordinate of the new move
# exceptions for the diagonals, 1, 3, 5, 7, 9

# Player 1 (O) always starts, Player 2 (X) is second

### Data ###

grid = """
        |     |
     1  |  2  |  3
   _____|_____|_____
        |     |
     4  |  5  |  6
   _____|_____|_____
        |     |
     7  |  8  |  9
        |     |
"""

num_to_coor = {
   "1": (0, 0),
   "2": (0, 1),
   "3": (0, 2),
   "4": (1, 0),
   "5": (1, 1),
   "6": (1, 2),
   "7": (2, 0),
   "8": (2, 1),
   "9": (2, 2),
}

### Game logic ###
class GameLogic:
   def __init__(self):
      self.board = [
         [None, None, None],
         [None, None, None],
         [None, None, None]
      ]
      self.game_over = False
      self.current_player = True
      self.num_of_plays = 0
      self.grid = """
         |     |
      1  |  2  |  3
    _____|_____|_____
         |     |
      4  |  5  |  6
    _____|_____|_____
         |     |
      7  |  8  |  9
         |     |
"""

   def play_move(self):
      if self.num_of_plays < 9:
         print(grid)
         play_input = input("Please type the number of the square you wish to play: ")

         while not self.validate_coor(play_input) and play_input != "r":
            print("Wrong input.")
            play_input = input("Please type the number of the square you wish to play: ")

         # Secret reset command
         if play_input == "r":
            self.reset_state()
            return

         self.update_board(play_input)
         self.update_grid(play_input)
         self.check_victory(play_input)

         if self.game_over:
            if self.current_player:
               player = "Player 1 (O)"
            else:
               player = "Player 2 (X)"
            print(f"{player} has won !")

         else:
            self.current_player = not self.current_player

      else:
         self.game_over = True
         print("Draw !")

      if self.game_over:
         reset_input = input("Type 'y' if you want to do another round: ")

         if reset_input == "y":
            self.reset_state()


   # Return True if the num given if valid, else False
   def validate_coor(self, num):
      if num in num_to_coor:
         row = num_to_coor[num][0]
         col = num_to_coor[num][1]

         if self.board[row][col] is None:
            return True

      return False


   # Update the state of the board
   def update_board(self, num):
      row = num_to_coor[num][0]
      col = num_to_coor[num][1]

      self.board[row][col] = self.current_player
      self.num_of_plays += 1


   # Update the grid with the player's symbol
   def update_grid(self, num):
      row = num_to_coor[num][0]
      col = num_to_coor[num][1]
      if self.current_player:
          symbol = "O"
      else:
          symbol = "X"

      self.grid = self.grid.replace(num, symbol)
      self.print_cleared_grid()


   # Print a version of the grid without the nums
   def print_cleared_grid(self):
      cleared_grid = self.grid
      for num in num_to_coor:
         cleared_grid = cleared_grid.replace(num, " ")

      print(cleared_grid)


   # Check the victory conditions, modify game_over to True if one player wins
   def check_victory(self, num):
      row = num_to_coor[num][0]
      col = num_to_coor[num][1]
      print(f"Num : {num} // row : {row} // col : {col}")

      self.game_over = (
         self.board[row][0] == self.board[row][1] == self.board[row][2]) or (
         self.board[0][col] == self.board[1][col] == self.board[2][col]
      )

      # Handling diagonals
      exceptions = ["1", "3", "5", "7", "9"]
      if num in exceptions:
         if num == "1" or num == "5" or num == "9":
            self.game_over = self.game_over or (
               self.board[0][0] == self.board[1][1] == self.board[2][2]
            )
         if num == "3" or num == "5" or num == "7":
            self.game_over = self.game_over or (
               self.board[0][2] == self.board[1][1] == self.board[2][0]
            )
      

   # Reset the state of the game
   def reset_state(self):
      self.board = [[None for elem in self.board[0]] for row in self.board]
      self.grid = grid
      self.game_over = False
      self.current_player = True
      self.num_of_plays = 0


### Execution ###
game = GameLogic()
while not game.game_over:
   game.play_move()