import numpy

N=int(input())

List1=[]
List2=[]

for i in range(N):
    a=list(map(int,input().split()))
    List1.append(a)

for i in range(N):
    b=list(map(int,input().split()))
    List2.append(b)

A=numpy.array(List1)
B=numpy.array(List2)
X=numpy.dot(A, B)

print(X)


# X=numpy.dot(A[0],A[1])
# print(X)
# Y=numpy.dot(B[0],B[1])
# print(Y)

# print(A)
# print(B)

