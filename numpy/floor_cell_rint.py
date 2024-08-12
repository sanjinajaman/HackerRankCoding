import numpy

A=list(map(float,input().split()))

Arr=numpy.array(A)
numpy.set_printoptions(sign=" ")

#floor print int only
'''
math.floor(x): Returns the floor of x, which is the largest integer less than or equal to x.
result = math.floor(4.7)
print(result)  # Output: 4
'''


print(numpy.floor(Arr))

'''
math.ceil(x): Returns the ceiling of x, which is the smallest integer greater than or equal to x.
import math

result = math.ceil(4.7)
print(result)  # Output: 5
'''

print(numpy.ceil(Arr))

'''
math.rint(x): Returns the nearest integer to x, rounding to even numbers in the case of a tie.
import math

result = math.rint(4.5)
print(result)  # Output: 4.0

result = math.rint(5.5)
print(result)  # Output: 6.0
'''
print(numpy.rint(Arr))

# print(Arr)