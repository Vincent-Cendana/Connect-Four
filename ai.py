from helper import wanted_states, search_matrix, sort_list_by_proximity_to_median
from re import search
import math

class AI:
  def __init__(self, depth=5):
    self.depth = depth

  def get_marker(self, current_depth):
    if current_depth % 2 == 0:
      return "X"
    else:
      return "O"

  def get_other_marker(self, marker):
    if marker == 'X':
      return 'O'
    else:
      return 'X'

  def get_best_move(self, board, current_depth, alpha, beta):
    current_marker = self.get_marker(current_depth)
    last_marker = self.get_other_marker(current_marker)
    
    board_terminal = board.terminal(last_marker)
    if board_terminal is True and last_marker == 'X':
      return float('inf')
    elif board_terminal is True and last_marker == 'O':
      return float('-inf')
    elif len(board.get_possible_moves()) == 0:
      return 0
    elif current_depth >= self.depth:
      return self.evaluate_board(board)

    # Put available moves into frontier
    available_moves = sort_list_by_proximity_to_median(board.get_possible_moves())
    possible_boards = []

    # Append possible states
    for move in available_moves:
      possible_boards.append(board.result(move, current_marker))

    if current_marker == 'X':
      max_index = 0
      max_val = float('-inf')
      # Append the values of those states
      for possible_board_i in range(len(possible_boards)):
        state_val = self.get_best_move(possible_boards[possible_board_i], 
                                         current_depth + 1, alpha, beta)
        if state_val > max_val:
          max_index = possible_board_i
          max_val = state_val
        alpha = max(alpha, state_val)
        if beta <= alpha:
          #print("Branch pruned at depth", current_depth)
          break
      if current_depth == 0:
        return available_moves[max_index]
      else:
        #print("Returned max")
        return max_val
    else:
      min_index = 0
      min_val = float('inf')
      # Append the values of those states
      for possible_board_i in range(len(possible_boards)):
        state_val = self.get_best_move(possible_boards[possible_board_i], 
                                         current_depth + 1, alpha, beta)
        if state_val < min_val:
          min_index = possible_board_i
          min_val = state_val
        beta = min(beta, state_val)
        if beta <= alpha:
          #print("Branch pruned at depth", current_depth)
          break
      if current_depth == 0:
        return available_moves[min_index]
      else:
        #print("Returned min")
        return min_val

  def evaluate_board(self, board):
    board_value = 0
    for state, point_value in wanted_states:
      num_instances = search_matrix(board.board, state)
      board_value += num_instances[0] * point_value
      board_value -= num_instances[1] * point_value

    middle_index = math.floor(len(board.board)/2)
    
    for row in range(len(board.board) - 1, -1, -1):
      if board.board[row][middle_index] == "X" and row % 2 == 1:
        board_value+=3
      elif board.board[row][middle_index] == "O" and row % 2 == 0:
        board_value-=3
    return board_value