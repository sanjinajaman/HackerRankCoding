import numpy
A=list(map(int, input().split()))
B=list(map(int,input().split()))
arr1=numpy.array(A)
arr2=numpy.array(B)

print(numpy.inner(arr1,arr2))
print(numpy.outer(arr1,arr2))
