'''import numpy
lis=list(input().split())
X=numpy.array(lis, float)


print(X[::-1])'''

import numpy

def arrays(arr):
   X=numpy.array(arr, float)
   return X[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)