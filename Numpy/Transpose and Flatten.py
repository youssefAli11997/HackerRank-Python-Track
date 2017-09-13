import numpy as np

n,m = map(int, input().split(' '))
arr = []

for i in range(n):
    arr += map(int, input().split(' '))

np_arr = np.array(arr, int).reshape((n,m))

print (np.transpose(np_arr))
print (np_arr.flatten()) # or just : print(arr)
