import numpy
N=tuple(map(int, input().split()))
#print(N)
#New_arr_shape=tuple(map(int, input().split()))
Arr=numpy.array(N)
#x=numpy.reshape(Arr,(New_arr_shape))
x=numpy.reshape(Arr,(3,3))
print(x)