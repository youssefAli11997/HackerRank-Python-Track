import numpy

def arrays(arr):
    return (numpy.array(arr,float))[::-1]
    # another solution :
    #arr.reverse()
    #return (numpy.array(arr,float))


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
