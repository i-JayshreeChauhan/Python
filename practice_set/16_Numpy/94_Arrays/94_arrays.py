import numpy


def arrays(arr):

    for index,i in enumerate(arr):  #convert all element to int
        arr[index] = float(arr[index])
    
    arr.reverse()
    a1 = numpy.array(arr)
    return a1


arr = input().strip().split(' ')
result = arrays(arr)
print(result)