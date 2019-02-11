import numpy as np
from util import timer_start, timer_stop, doubleArray
import core.calc as calc

def dist(a, b):
    c = a-b
    return np.sqrt(np.dot(c, c))
def dist2(a, b):
    c = a-b
    return np.sqrt(np.sum(c*c))
def dist3(a, b):
    return np.linalg.norm(a-b)
def dist4(a, b):
    c = a-b
    return np.dot(c, c)**(1/2)
def dist5(a, b):
    return calc.dist(doubleArray(a), doubleArray(b), len(a))

rand_min = -100
rand_max = 100
dim = 3

u_vectors = []
v_vectors = []
print('Constructing random vector list...')
timer_start()
for i in range(1000000):
    u_vectors.append(np.random.random_integers(rand_min, rand_max, (dim,)))
    v_vectors.append(np.random.random_integers(rand_min, rand_max, (dim,)))
timer_stop('Completed random vector list construction')

print('sample: u='+str(u_vectors[0])+',v='+str(v_vectors[0]))

# # M1
# timer_start()
# for n in range(len(u_vectors)):
#     v = dist(u_vectors[n], v_vectors[n])
# timer_stop('M1')
#
# # M2
# timer_start()
# for n in range(len(u_vectors)):
#     v = dist2(u_vectors[n], v_vectors[n])
# timer_stop('M2')
#
# # M3
# timer_start()
# for n in range(len(u_vectors)):
#     v = dist3(u_vectors[n], v_vectors[n])
# timer_stop('M3')
#
# # M4
# timer_start()
# for n in range(len(u_vectors)):
#     v = dist4(u_vectors[n], v_vectors[n])
# timer_stop('M4')

# M5
timer_start()
for n in range(len(u_vectors)):
    v = dist5(u_vectors[n].astype(dtype=np.float64), v_vectors[n].astype(dtype=np.float64))
timer_stop('M5')
