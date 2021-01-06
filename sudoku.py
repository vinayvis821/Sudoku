import pygame

def print_board( grid ):
    for i in range(9):
        if i % 3 == 0 and i != 0 :
            print( "-----------------------")
        for j in range(9):
            if j % 3 == 0 and j!= 0:
                print( " | ", end= '' )
            if j == 8:
                print( grid[i][j] )
            else:
                print( str(grid[i][j]) + " ", end = '')


def find_next_avail( grid ):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return (r, c)
    return None, None
    

def validate( grid, row, col, guess ):
    # check if num is in the row
    row_list = grid[row]
    if guess in row_list:
        return False
        
    # check if num is in the column
    for i in range(len(grid)):
        if grid[row][i] == guess:
            return False
        
    # check 3 by 3 matrix
    row = (row // 3) * 3
    col = (col // 3) * 3
    for r in range(row, row+3):
        for c in range(col, col+3):
            if grid[r][c] == guess:
                return False

    return True


def solver( grid ):
    row, col = find_next_avail( grid )
    if row is None:
        return True 
    
    for guess in range(1, 10):
        val = validate( grid, row, col, guess )
        if val:
            grid[row][col] = guess
            if solver( grid ):
                return True
        grid[row][col] = 0
    return False


if __name__ == '__main__':
    grid = [[ 0, 0, 5,    8, 0, 9,    4, 7, 0],
            [ 0, 2, 0,    0, 6, 0,    0, 0, 1],
            [ 0, 7, 0,    0, 0, 0,    0, 6, 9],

            [ 4, 0, 0,    0, 0, 0,    1, 0, 0],
            [ 0, 0, 2,    1, 0, 8,    9, 0, 6],
            [ 3, 0, 0,    9, 4, 0,    0, 2, 8],

            [ 2, 3, 0,    7, 5, 0,    6, 9, 4],
            [ 5, 0, 0,    0, 0, 3,    8, 0, 0],
            [ 6, 9, 0,    0, 0, 2,    3, 5, 0]]     
    print_board( grid )
    print( solver( grid ) )
    print_board( grid )


# Empty board to use
#    [[ 0, 0, 0,    0, 0, 0,    0, 0, 0],
#     [ 0, 0, 0,    0, 0, 0,    0, 0, 0],
#     [ 0, 0, 0,    0, 0, 0,    0, 0, 0],

#     [ 0, 0, 0,    0, 0, 0,    0, 0, 0],
#     [ 0, 0, 0,    0, 0, 0,    0, 0, 0],
#     [ 0, 0, 0,    0, 0, 0,    0, 0, 0],

#     [ 0, 0, 0,    0, 0, 0,    0, 0, 0],
#     [ 0, 0, 0,    0, 0, 0,    0, 0, 0],
#     [ 0, 0, 0,    0, 0, 0,    0, 0, 0]]
    
   
