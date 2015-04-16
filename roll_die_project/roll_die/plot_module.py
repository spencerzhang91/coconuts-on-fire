from matplotlib import pyplot as plt
from roll_die_module import roll_die

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
