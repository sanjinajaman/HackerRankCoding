
import numpy as np
#N means first row num and M is last row and P is num of col

N, M, P= map(int,input().split())
list1=[]
list2=[]

#print(N,M,P)

for i in range(N):
    a=list(map(int, input().split()))
    list1.append(a)

for i in range(M):
    b=list(map(int, input().split()))
    list2.append(b)

array_1 = np.array(list1)
array_2 = np.array(list2)
# print(type(array_1))
# print(array_2)
print (np.concatenate((array_1, array_2) , axis=0))

#print ((list1+ list2))
