def sudoku(puzzle):
    empty = find_empty(puzzle)
    if not empty:
        return True
    else:
        row, col = empty

    for num in range(1, 10):
        if is_valid(puzzle, num, (row, col)):
            puzzle[row][col] = num

            if sudoku(puzzle):
                return puzzle
            
            puzzle[row][col] = 0

    return False

def find_empty(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return(i, j)
    return None

def is_valid(puzzle, num, pos):
    for i in range(9):
        if puzzle[pos[0]][i] == num and i != pos[1]:
            return False
        
    for i in range(9):
        if puzzle[i][pos[1]] == num and i != pos[0]:
            return False
    
    box_x = pos[1] // 3
    box_y = pos[0] // 3 
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if puzzle[i][j] == num and (i, j) != pos:
                return False

    return True


puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]


print(sudoku(puzzle))
