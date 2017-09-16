import numpy as np

a = map(int, input().split())
a = tuple(a)
np_arr = np.zeros(a, dtype = np.int)
np_arr2 = np.ones(a, dtype = np.int)
print(np_arr)
print(np_arr2)
