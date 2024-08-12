import numpy

N , M= map(int, input().split())
List=[]
for i in range (N):
     l=list(map(int, input().split()))
     List.append(l)
arr=numpy.array(List)
print(arr)
x=numpy.min((arr), axis=1)
print(x)
print(numpy.max((x), axis=0))