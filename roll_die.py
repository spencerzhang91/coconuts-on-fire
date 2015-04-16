import random
import matplotlib.pyplot as plt

def roll_die(side_num):
    '''
    The input argument represents the sides of an abstract die which
    could be normal six-sided die otherwise with more or less sides in
    spite of physical feasibility.
    '''
    return random.randint(1, side_num)

def test_roll(side_num, roll_num):
    '''
    Roll a die with side_num sides roll_num times.
    '''
    print('Roll a %d sided die %d times.' % (side_num, roll_num))
    for i in range(roll_num):
        roll = roll_die(side_num)
        print('Roll is', str(roll))

# test_roll(6,10)

trial_stride = 5
def plot_fairness(side, side_num, max_trials):
    '''
    Plot the mathematical probability for an outcome vs. computed
    estimate.
    '''
    x, y, z= [], [], []
    for trial_num in range(trial_stride, max_trials, trial_stride):
        side_count = 0
        for i in range(trial_num):
            if roll_die(side_num) == side:
                side_count += 1
        mathematical = 1 / side_num
        computed = side_count / trial_num
        x.append(trial_num)
        y.append((computed - mathematical)/mathematical)
        z.append(0)
    plt.plot(x, z, 'r-')
    plt.plot(x, y, 'b-')
    plt.ylim(-1.0, 1.0)
    plt.xlim(0, 2000)
    plt.title('Fairness Test')
    plt.xlabel('Roll numbers')
    plt.ylabel('Bials')
    plt.show()

a = plot_fairness(3, 6, 2000)
print(a)
