import numpy as np

n,m = map(int, input().split())
np_arr = np.array([input().split() for i in range(n)], int)
print(np.prod(np.sum(np_arr, axis=0)))
