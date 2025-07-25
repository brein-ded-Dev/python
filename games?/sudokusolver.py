
def block_correct(sudoku: list, row_no: int, column_no: int):
    block = []
    for i in range (3):
        for j in range(3):
            value = sudoku[row_no + i][column_no + j]
            if value != 0 and value in block:
                return False
            block.append(value)
    return True

def column_correct(sudoku: list, column_no: int):
    column = []
    for i in range(len(sudoku)):
        if sudoku[i][column_no] !=0 and sudoku[i][column_no] in column:
            return False
        column.append(sudoku[i][column_no])
    return True


def row_correct(sudoku: list, row_no: int):
    for i in sudoku[row_no]:
        duplicates = 1
        if i == 0:
            continue
        for j in sudoku[row_no]:
            if i == j and i != 0:
                duplicates -= 1
        if duplicates < 0:
            return False
        
    
    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(len(sudoku)):
        if not row_correct(sudoku, i):
            return False
        if not column_correct(sudoku, i):
            return False
    
    for i in range(0, len(sudoku), 3):
        for j in range(0, len(sudoku), 3):
            if not block_correct(sudoku, i, j):
                return False
    
    return True


#0 represents an empty cell in the sudoku grid
sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(sudoku_grid_correct(sudoku1))

sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]

print(sudoku_grid_correct(sudoku2))