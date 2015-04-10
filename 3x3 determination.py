def determination(m):
    '''
    A function that calculates the determination of 3 by 3 matrix.
    '''
    res = m[0][0] * m[1][1] * m[2][2] + \
          m[0][1] * m[1][2] * m[2][0] + \
          m[0][2] * m[1][0] * m[2][1] - \
          m[0][2] * m[1][1] * m[2][0] - \
          m[0][0] * m[1][2] * m[2][1] - \
          m[0][1] * m[1][0] * m[2][2]

    return res





matrix = [[-1,-2,0],
          [4,-1,2],
          [-1,4,-1]
          ]

test = determination(matrix)
print('The determination of inputed matrix is:', test)
