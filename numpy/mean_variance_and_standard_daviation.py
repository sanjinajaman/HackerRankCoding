import numpy

N,M=map(int, input().split())
List=[]
for i in range(N):
    list1=list(map(int, input().split()))
    List.append(list1)
# print(List)


Arr=numpy.array(List)

print(numpy.mean((Arr),axis=1))
print(numpy.var((Arr),axis=0))
print(round(numpy.std(Arr, axis=None),11))

# print(Arr)

