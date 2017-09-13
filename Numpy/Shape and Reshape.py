import numpy as np

arr = input().split(' ')
np_arr = np.array(arr, int).reshape((3,3))

print(np_arr)
