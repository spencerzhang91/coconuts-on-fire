# A silly implementation of Christmas Tree
# Merry Christmas everyone!!

def ChristmasTree(line, seg):
    m = 0
    indent = 32
    gift = []
    for n in range(seg):
        for i in range(line // seg):
            santa = (4 * (i + m) + 1)
            gift.append(santa)
        m += 1
    for x in range(len(gift)):
        print(' ' * (gift[-(x+1)] // 2 + indent) + '*' * gift[x])
    print((' ' * (gift[-1] // 2 - 1 + indent) + '|||\n') * (line // 4))
    

# Let's grow a Christmas tree~
ChristmasTree(20,3)






