def count_neighbours(grid, i, j):
    L = []
    m = len(grid)
    n = len(grid[0])
    point = (i,j)
    pos_list = [(i-1+x, j-1+y) for x in range(3) for y in range(3) \
                if (m-1 >= (i-1+x) >= 0 and n-1 >= (j-1+y) >= 0)]
    pos_list.remove(point)
    for pos in pos_list:
        if grid[pos[0]][pos[1]] == 1:
            L.append(grid[pos[0]][pos[1]])
    return len(L)

# test

grid_1 = ((1, 0, 0, 1, 0),
          (0, 1, 0, 0, 0),
          (0, 0, 1, 0, 1),
          (1, 0, 0, 0, 0),
          (0, 0, 1, 0, 0))



test = count_neighbours(grid_1, 3, 4)
print(test)       

# 感觉是一个更加厉害的方法（其实就是用了高级武器）
'''
from itertools import product
neighbours = [ (dy,dx) for dx,dy in product([-1,0,1],repeat=2) if dx or dy ]
def count_neighbours(grid, row, col):
    return sum( grid[row+dy][col+dx] for dy, dx in neighbours
                if 0 <= row + dy < len(grid) and 0 <= col + dx < len(grid[0]) )

'''
