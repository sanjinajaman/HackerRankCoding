import numpy

N, M=map(int, input().split())

List1=[]
List2=[]

for i in range(N):
    l=list(map(int, input().split()))
    List1.append(l)

for i in range(N):
    l=list(map(int, input().split()))
    List2.append(l)


Arr1=numpy.array(List1)
# print(Arr1)

Arr2=numpy.array(List2)
# print(Arr2)

Arr_add=numpy.add(Arr1,Arr2)
print(Arr_add)
Arr_subtract=numpy.subtract(Arr1,Arr2)
print(Arr_subtract)

Arr_multiply=numpy.multiply(Arr1,Arr2)
print(Arr_multiply)

Arr_divide=numpy.floor_divide(Arr1,Arr2)

print(Arr_divide)
Arr_mod=numpy.mod(Arr1,Arr2)
print(Arr_mod)
Arr_power=numpy.power(Arr1,Arr2)
print(Arr_power)