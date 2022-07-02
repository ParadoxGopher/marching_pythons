from this import d
from numba import cuda, int32
import numpy as np


TBP = 16


@cuda.jit
def add_uf(x, y, r):
    i = cuda.grid(1)

    r[i] = x[i]+y[i]


a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
c = np.zeros([4])

aD = cuda.to_device(a)
bD = cuda.to_device(b)
cD = cuda.to_device(c)

add_uf[1, TBP](aD, bD, cD)
c = cD.copy_to_host()
print('a+b:\n', c)
