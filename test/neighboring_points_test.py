import numpy as np
from util import neighboring_points, timer_start, timer_stop

n = 1000000
arr = np.random.random((2,))*200-100
print(arr)
print(neighboring_points(arr))
print('Running neigboring_points '+str(n)+' times')
timer_start()
for i in range(n):
    neighboring_points(np.random.random((2,))*200-100)
timer_stop('Finished')
