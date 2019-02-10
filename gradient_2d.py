import random

from vector import *
import math
import numpy as np
import sys

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
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + ' ' * (length - filledLength)
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    # Print New Line on Complete
    if iteration == total:
        print()
    sys.stdout.flush()

size = 300
gradient = np.fromfunction(np.vectorize(lambda x: -abs(x-size/2)+size/2+(1/100.0)*((x-size/2))**2), (size,), dtype=np.float32)
in_arr = np.random.random(gradient.shape).astype(dtype=np.float32)
in_arr = (in_arr - np.mean(in_arr)) / np.std(in_arr)

def gf(x3):
    if len(gradient)-1 > x3 >= 0:
        if math.floor(x3) == x3:
            return gradient[x3]
        else:
            x1 = math.floor(x3)
            x2 = math.ceil(x3)
            y1 = gradient[x1]
            y2 = gradient[x2]
            return (y2 - y1) * ((x3 - x1) / (x2 - x1)) + y1
    elif len(gradient)-1 == x3:
        return gradient[x3]
    else:
        return math.nan

class Signal2D:
    def __init__(self):
        self.position = Vector2D(0, 0)
        self.velocity = Vector2D(0, 0)
        self.radius = np.float32(0)

    def __str__(self):
        return 'Signal2D{position='+str(self.position)+';velocity='+str(self.velocity)+';radius='+str(self.radius)+'}'

input_data = np.random.rand(len(gradient))
input_data = (input_data - np.mean(input_data)) / np.std(input_data)
signals = np.empty(gradient.shape, dtype=Signal2D)
for i in range(len(signals)):
    s = Signal2D()
    s.position.x = i
    s.position.y = gf(s.position.x)
    s.radius = input_data[i]

    signals[i] = s


frame_count = 1000

gravity = Vector2D(0, -1)
friction = 1.1
terrain_modification = True
terrain_effect_factor = 0.01
zero_magnitude_threshold = 0.03

signal_graph_file = open('E:/latest.csv', 'w+')
terrain_graph_file = open('E:/terrain_graph.csv', 'w+')

csv_line = ''
for signal_index in range(len(signals)):
    csv_line += 'x'+str(signal_index)+','
    csv_line += 'y'+str(signal_index)
    if signal_index != len(signals)-1:
        csv_line += ','
csv_line += '\n'
terrain_csv_line = ''
for terrain_point_index in range(len(gradient)):
    terrain_csv_line += str(terrain_point_index)
    if terrain_point_index != len(signals)-1:
        terrain_csv_line += ','
terrain_csv_line += '\n'

for frame_number in range(frame_count):
    print_progress_bar(frame_number, frame_count, prefix=str(frame_number)+'/'+str(frame_count))
    for signal_index in range(len(signals)):
        s = signals[signal_index]
        if math.isnan(s.position.y):
            continue
        result = gravity.add(s.velocity)
        # slope = Vector2D(2*d, gf(position.x+d)-gf(position.x-d))
        if len(gradient)-1 > s.position.x >= 0:
            sx = math.ceil(s.position.x)
            ex = math.floor(s.position.x)
            if ex == sx:
                ex -= 1
            slope = Vector2D(1, gradient[sx]-gradient[ex])
            delta = result.project_onto(slope).divide(friction)
        else:
            delta = result

        s.velocity = delta
        if s.velocity.magnitude() < zero_magnitude_threshold:
            s.velocity.x = 0
            s.velocity.y = 0
            # TODO: Delete when done
            s.position.x = random.random()*len(gradient)
            s.position.y = gf(s.position.x)

        before_x = s.position.x
        before_y = s.position.y
        s.position.x += s.velocity.x
        s.position.y = gf(s.position.x)
        after_x = s.position.x
        after_y = s.position.y

        # Terrain modification algorithm
        terrain_change = terrain_effect_factor * s.radius
        for i in range(math.floor(min(before_x, after_x)), math.floor(max(before_x, after_x))):
            if len(gradient) > i >= 0:
                gradient[i] += terrain_change

        csv_line += str(s.position.x) + ','
        if math.isnan(s.position.y):
            pass
        else:
            csv_line += str(s.position.y)
        if signal_index != len(signals)-1:
            csv_line += ','

    for terrain_point_index in range(len(gradient)):
        terrain_csv_line += str(gradient[terrain_point_index])
        if terrain_point_index != len(gradient)-1:
            terrain_csv_line += ','

    signal_graph_file.write(csv_line + '\n')
    csv_line = ''
    terrain_graph_file.write(terrain_csv_line+'\n')
    terrain_csv_line = ''

signal_graph_file.close()
