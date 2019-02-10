import time
import numpy as np
import math

def current_time_millis():
    """Returns the current time in milliseconds since the epoch"""
    return int(round(time.time() * 1000))

start_time = 0
def timer_start():
    """Starts the global utility timer"""
    global start_time
    start_time = current_time_millis()
def timer_stop(msg):
    """Stops the global utility timer, printing out a message followed by 'in ___ ms'"""
    print(msg + ' in '+str(current_time_millis()-start_time)+' ms')

def dist(a, b):
    """Calculates the distance between two points

    Both inputs must be of the same
    length, and should also only be 1 dimensional"""
    c = a-b
    return np.sqrt(np.dot(c, c))

def neighboring_points(pos):
    """Finds all neighboring points to a position and performs an operation on them

    To see more details, visit the TopologicalComputer notebook and see
    Planning > GradientND > Terrain Modification"""

    int_pos = pos.astype(np.int32).tolist()
    n = len(int_pos)
    i = 2**n - 1
    points = np.empty((i+1, n), dtype=np.int32)
    digits = np.arange(0, n)
    # powers = 2 ** digits
    # print(powers)
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
