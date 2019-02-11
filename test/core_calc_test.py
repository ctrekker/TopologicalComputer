import core.calc as calc
import util
import numpy as np

def main():
    test_dist()

def test_dist():
    '''Testing function for the dist methods within the calc core module
    
    Creates two arrays of random nth dimensional vectors and uses the 
    calc.dist_batch method to calculate and get the distances between
    all the points'''
    quantity = 1000000
    rand_min = -100
    rand_max = 100
    dim = 3

    print('Quantity: '+str(quantity))
    print('Constructing random vector list...')
    util.timer_start()
    # u_vectors = []
    # v_vectors = []
    u_vectors = calc.doubleArray(quantity * dim)
    v_vectors = calc.doubleArray(quantity * dim)
    for i in range(quantity):
        if i % 1000 == 0:
            util.print_progress_bar(i, quantity)
        # u_vectors.append(util.doubleArray(np.random.random_integers(rand_min, rand_max, (dim,)).astype(dtype=np.float64)))
        # v_vectors.append(util.doubleArray(np.random.random_integers(rand_min, rand_max, (dim,)).astype(dtype=np.float64)))
        u_tmp = np.random.random_integers(rand_min, rand_max, (dim,)).astype(dtype=np.float64)
        v_tmp = np.random.random_integers(rand_min, rand_max, (dim,)).astype(dtype=np.float64)
        for j in range(dim):
            u_vectors[i * dim + j] = u_tmp[j]
            v_vectors[i * dim + j] = v_tmp[j]

    util.timer_stop('Completed random vector list construction', progress_bar=True)

    # for i in range(quantity):
    #     v = calc.dist(u_vectors[i], v_vectors[i], dim)
    print('Vector u[0]: '+str(u_vectors[0])+','+str(u_vectors[1])+','+str(u_vectors[2]))
    print('Vector v[0]: '+str(v_vectors[0])+','+str(v_vectors[1])+','+str(v_vectors[2]))

    util.timer_start()
    batch = calc.dist_batch(u_vectors, v_vectors, dim, quantity * dim)
    batch = calc.doubleArray_frompointer(batch)
    util.timer_stop('M5')

    print('Result: '+str(batch[0]))

    # print(calc.dist(a, b, 3))

if __name__ == '__main__':
    main()
