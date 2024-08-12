import numpy
#You are given an X integer array matrix with space separated elements ( = rows and  = columns).
N,M=map(int, input().split())

List=[]

for i in range(N):
    l=list(map(int, input().split()))
    List.append(l)

Arr=numpy.array(List)

print(numpy.transpose(Arr))
#print(numpy.flatiter(Arr) )
print(Arr.flatten() )