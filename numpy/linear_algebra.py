import numpy

N=int(input())
List=[]

for i in range(N):
    l=list(map(float, input().split()))
    List.append(l)

Arr=numpy.array(List)

print(round(numpy.linalg.det(Arr),2))
#this line take input different way for example vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
# print(numpy.linalg.eig(Arr))
#print(numpy.linalg.inv(Arr))