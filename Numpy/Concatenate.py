import numpy as np

n,m,p = map(int, input().split())
arr1 = [input().split() for i in range(n)] 
arr2 = [input().split() for i in range(m)]

np_arr = np.concatenate((np.array(arr1, int), np.array(arr2, int)), axis=0)
print(np_arr)
