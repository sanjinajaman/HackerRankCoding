import numpy


M, N= map(int,input().split())
List=[]

for i in range(M):
    l=list(map(int, input().split()))
    List.append(l)
#print(List)

arr=numpy.array(List)
print(arr)
x=numpy.sum((List), axis=0)
print(numpy.prod((x), axis=None))
