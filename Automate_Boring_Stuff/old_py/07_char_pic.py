grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#for each column first
#test 2d length? number of rows below
rows = len(grid)
#columns, don't like this, won't work for jagged 2ds...
cols = len(grid[0])

for j in range(cols):
    for i in range(rows):
        print(grid[i][j], end='')
    print()
