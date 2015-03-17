def j(L):
    x_pos = []; o_pos = []
    for i in range(3):
        for j in range(3):
            if L[i][j] == 'X':
                x_pos.append((i,j))
            elif L[i][j] == 'O':
                o_pos.append((i,j))              
    x_row = [item[0] for item in x_pos]
    x_col = [item[1] for item in x_pos]
    o_row = [item[0] for item in o_pos]
    o_col = [item[1] for item in o_pos]
    if x_row.count(0) == 3 or x_row.count(1) == 3 or x_row.count(2) == 3:
        xw = 1
    elif x_col.count(0) == 3 or x_col.count(1) == 3 or x_col.count(2) == 3:
        xw = 1
    elif (0,0) in x_pos and (1,1) in x_pos and (2,2) in x_pos:
        xw = 1
    elif (0,2) in x_pos and (1,1) in x_pos and (2,0) in x_pos:
        xw = 1
    else:
        xw = 0
    if o_row.count(0) == 3 or o_row.count(1) == 3 or o_row.count(2) == 3:
        ow = 1
    elif o_col.count(0) == 3 or o_col.count(1) == 3 or o_col.count(2) == 3:
        ow = 1
    elif (0,0) in o_pos and (1,1) in o_pos and (2,2) in o_pos:
        ow = 1
    elif (0,2) in o_pos and (1,1) in o_pos and (2,0) in o_pos:
        ow = 1
    else:
        ow = 0
    if xw > ow:
        return "X"
    elif xw < ow:
        return "O"
    else:
        return "D"

L1 = ["X.O","XX.","XOO"]
L2 = ['OO.','XOX','XOX']
L3 = ['OOX','XXO','OXX']

print(j(L1),j(L2),j(L3))


# 更好的解法来了，虽然不是最好，但是比我的简洁多了。。。
'''
def checkio(game_result):
    #row
    for row in game_result:
        if row[0] == row[1] == row[2] != ".":
            return row[0]
    #column
    for col in zip(*game_result):
        if col[0] == col[1] == col[2] != ".":
            return col[0]
​
    #diagonal
    if game_result[0][0] == game_result[1][1] == game_result[2][2] != ".":
        return game_result[0][0]
    if game_result[0][2] == game_result[1][1] == game_result[2][0] != ".":
        return game_result[0][2]
​
    return "D"
'''
