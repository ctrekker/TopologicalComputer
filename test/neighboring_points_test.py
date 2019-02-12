import numpy as np
from util import neighboring_points, timer_start, timer_stop
import util
import core.calc as calc

n = 100000
dim = 3
arr1 = []
arr2 = []
print('Building random positions...')
timer_start()
for i in range(n):
    arr1.append(np.random.random((dim,))*200-100)
    arr2.append(util.doubleArray(np.random.random((dim,))*200-100))
timer_stop('Finished building random positions')

print('Running python neighboring_points '+str(n)+' times')
timer_start()
for i in range(n):
    neighboring_points(arr1[i])
timer_stop('Finished python neighboring_points')

print('Running C++ binding neighboring_points '+str(n)+' times')
timer_start()
for i in range(n):
    calc.neighboring_points(arr2[i], dim)
timer_stop('Finished C++ binding neighboring_points')
