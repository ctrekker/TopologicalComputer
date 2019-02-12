import time
import numpy as np
import core.calc as calc
import sys

def current_time_millis():
    """Returns the current time in milliseconds since the epoch"""
    return int(round(time.time() * 1000))

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='='):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + ' ' * (length - filled_length)
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    # Print New Line on Complete
    if iteration == total:
        print()
    sys.stdout.flush()

start_time = 0
def timer_start():
    """Starts the global utility timer"""
    global start_time
    start_time = current_time_millis()
def timer_stop(msg, progress_bar=False):
    """Stops the global utility timer, printing out a message followed by 'in ___ ms'"""
    sys.stdout.write('\r');
    print(msg + ' in '+str(current_time_millis()-start_time)+' ms')

def doubleArray(arr):
    a = calc.doubleArray(len(arr))
    for b in range(len(arr)):
        a[b] = arr[b]
    return a
def intArray(arr):
    a = calc.doubleArray(len(arr))
    for b in range(len(arr)):
        a[b] = arr[b]
    return a
def print_array(arr, length, start=0):
    sys.stdout.write('[')
    for i in range(start, start+length):
        sys.stdout.write(str(arr[i])+',')
    sys.stdout.write(']\n')

def dist(a, b):
    """Calculates the distance between two points

    Both inputs must be of the same
    length, and should also only be 1 dimensional

    NOTE: This should only be used for testing. Use C++ binding for prod"""
    c = a-b
    return np.sqrt(np.dot(c, c))

def neighboring_points(pos):
    """Finds all neighboring points to a position and performs an operation on them

    To see more details, visit the TopologicalComputer notebook and see
    Planning > GradientND > Terrain Modification

    NOTE: This should only be used for testing. Use C++ binding for prod"""

    int_pos = pos.astype(np.int32).tolist()
    n = len(int_pos)
    i = 2**n - 1
    points = np.empty((i+1, n), dtype=np.int32)
    signs = np.sign(int_pos).tolist()
    placeholders = [0] * n
    for digit in range(n):
        placeholders[digit] = 2 ** digit
    # print(placeholders)
    for a in range(i+1):
        index = np.empty((n,), dtype=np.int32)

        for digit in range(n):
            # index[digit] = math.floor(pos[digit]) if ((a & 2 ** digit) >> digit) == 0 else math.ceil(pos[digit])
            index[digit] = int_pos[digit] + ((a & placeholders[digit]) >> digit) * signs[digit]
            # index[digit] = int_pos[digit] + (a & placeholders[digit])
        points[a] = index
    return points
