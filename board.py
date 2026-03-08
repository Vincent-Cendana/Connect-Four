from helper import win_states, search_matrix
import copy

class Board:
  def __init__(self, rows=3, cols=3, board=None):
    if board:
      self.board = board
    else:
      self.board = []
      for row_i in range(rows):
        self.board.append([])
        for _ in range(cols):
          self.board[row_i].append("-")

  def __repr__(self):
    board_repr = ""
    for row in self.board:
      board_repr += '[' + ' '.join(row).replace('\'', ' ') + ']\n'
    col_repr = str(list(range(1, len(self.board[0])+1)))
    board_repr += ''.join(col_repr).replace(',', '') + '\n'
    return board_repr

  def get_possible_moves(self):
    possible_moves = []
    for i in range(len(self.board[0])):
      if self.board[0][i] == "-":
        possible_moves.append(i)

    return possible_moves

  def place(self, col, marker):
    for row in range(len(self.board) - 1, -1, -1):
      if self.board[row][col] == "-":
        self.board[row][col] = marker
        return self.board

  def result(self, col, marker):
    fake_board = Board(board=copy.deepcopy(self.board))
    fake_board.place(col, marker)
    return fake_board

  def terminal(self, wanted_symbol):
    instance_index = 0 if wanted_symbol == 'X' else 1
    state_won = True in (search_matrix(self.board, state)[instance_index] > 0
                         for state in win_states)
    return state_won