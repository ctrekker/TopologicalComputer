import time
import numpy as np

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
