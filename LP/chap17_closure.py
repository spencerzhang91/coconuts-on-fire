def makemovement(name, origin, pace):
    x = origin[0]
    y = origin[1]
    def movement(direction):
        nonlocal x, y
        if direction == 'N':
            y -= pace
        elif direction == 'S':
            y += pace
        elif direction == 'E':
            x += pace
        elif direction == 'W':
            x -= pace
        else:
            raise directionError
        print("%s's New position: (%d, %d)\n" % (name, x, y))
    return movement

if __name__ == "__main__":
    player_one = makemovement('Sam', (0, 0), 2)
    player_two = makemovement('James', (4, 3), 3)
    player_one('N')
    player_two('W')
