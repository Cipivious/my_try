import numpy
import random

arr = numpy.array(range(20))
print(arr)
arr1 = numpy.reshape(arr, (4, 5))
print(arr1)
print(arr.shape)
arr2 = numpy.reshape(arr, (arr1.shape[0] * arr1.shape[1],))
print(arr2)
arr3 = numpy.asarray(arr, dtype="float32")
print(arr3)
arr4 = numpy.array(range(20), dtype="int8")
arr5 = numpy.ones((3, 4)) * 5
print(arr5)
# 广播机制
arr6 = numpy.array(
    [[random.random(), random.random(), random.random()] for i in range(4)]
)
print(arr6)
arr7 = numpy.array(
    [
        [[random.random(), random.random(), random.random()] for i in range(4)]
        for j in range(2)
    ]
)
print(arr7)
print(arr7 + arr6)
