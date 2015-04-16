def test_roll(side_num, roll_num):
    '''
    Roll a die with side_num sides roll_num times.
    '''
    print('Roll a %d sided die %d times.' % (side_num, roll_num))
    for i in range(roll_num):
        roll = roll_die(side_num)
        print('Roll is', str(roll))
