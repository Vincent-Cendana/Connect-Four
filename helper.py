import statistics

def search_matrix(matrix, wanted_image):
  x_instances = 0
  o_instances = 0

  row_range = len(matrix) - len(wanted_image) + 1
  col_range = len(matrix[0]) - len(wanted_image[0]) + 1

  for row_i in range(row_range):
    for col_i in range(col_range):
      matrix_slice = [
          row[col_i:col_i + len(wanted_image[0])]
          for row in matrix[row_i:row_i + len(wanted_image)]
      ]
      if simplify(matrix_slice, wanted_image, 'X')==wanted_image:
        x_instances+=1
      elif simplify(matrix_slice, wanted_image, 'O')==wanted_image:
        o_instances+=1

  return x_instances, o_instances

def simplify(matrix, mask, ignore):
  new_matrix = []
  for row_i in range(len(matrix)):
    new_matrix.append([
      'P' 
      if matrix[row_i][col_i] == ignore 
      and mask[row_i][col_i] == 'P'
      else '-' 
      for col_i in range(len(matrix[row_i]))
    ])
  return new_matrix

# Created with AI with promopt "create a function to sort a list beginning with 
# those closest with the median"

def sort_list_by_proximity_to_median(input_list):
  median = statistics.median(input_list)
  return sorted(input_list, key=lambda x: abs(x-median))

win_states = (
  [['P'], ['P'], ['P'], ['P']],
  [['P', 'P', 'P', 'P']],
  [
    ['P', '-', '-', '-'],
    ['-', 'P', '-', '-'],
    ['-', '-', 'P', '-'],
    ['-', '-', '-', 'P']
  ],
  [
    ['-', '-', '-', 'P'],
    ['-', '-', 'P', '-'],
    ['-', 'P', '-', '-'],
    ['P', '-', '-', '-']
  ]
)

wanted_states = (
  ([['P'], ['P'], ['P']], 15),
  ([['P', 'P', 'P']], 15),
  ([
    ['-', '-', 'P'],
    ['-', 'P', '-'],
    ['P', '-', '-'],
  ], 15),
  ([
    ['P', '-', '-'],
    ['-', 'P', '-'],
    ['-', '-', 'P']
    ], 15),
  ([
    ['P', 'P', 'P'],
    ['-', 'P', '-'],
    ['-', '-', 'P']
  ], 40),
  ([
    ['P', 'P', 'P'],
    ['-', 'P', '-'],
    ['P', '-', '-']
  ], 40),
  ([['P'], ['P']], 1),
  ([['P', 'P']], 1),
  ([
    ['P', '-'],
    ['-', 'P']
  ], 2),
  ([
    ['-', 'P'],
    ['P', '-']
  ], 2)
)