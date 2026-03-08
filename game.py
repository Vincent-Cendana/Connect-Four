from board import Board
from ai import AI
import time


class Game:

  def __init__(self, board=None):
    self.board = Board(6, 7, board=board)
    self.turn = 1
    self.enemy_player = AI(5)

  def start(self):
    while len(self.board.get_possible_moves()) > 0:
      start = time.time()
      print("Enemy Thinking...")
      best_enemy_move = self.enemy_player.get_best_move(
          self.board, 0, float('-inf'), float('inf'))
      self.board.place(best_enemy_move, 'X')
      print("Elapsed time: ", time.time() - start)
      print("Enemy went column", best_enemy_move+1)
      print(self.board)
      user_col = int(input('Input col: '))
      self.board.place(user_col - 1, 'O')
      self.turn += 1
    print(self.board)
