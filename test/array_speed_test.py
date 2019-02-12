import core.calc as calc
import numpy as np
from util import timer_start, timer_stop, doubleArray

size = 1000000

# Define / init arrays
timer_start()
array1 = [0.0] * size
timer_stop('Created array1')

timer_start()
array2 = np.zeros((size,), dtype=np.float64)
timer_stop('Created array2')

timer_start()
array3 = calc.doubleArray(size)
for x in range(size):
    array3[x] = 0.0
timer_stop('Created array3')


# Modify values in arrays
def modify_array(arr, length):
    for y in range(0, length):
        arr[y] = y

timer_start()
modify_array(array1, size)
timer_stop('Modified array1')

timer_start()
modify_array(array2, size)
timer_stop('Modified array2')

timer_start()
modify_array(array3, size)
timer_stop('Modified array3')

timer_start()
doubleArray(array1)
timer_stop('Converted array1 to array3')

timer_start()
doubleArray(array2)
timer_stop('Converted array2 to array3')
