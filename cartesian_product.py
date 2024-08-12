from itertools import product
A=list(map(int , input().split()))

B=list(map(int , input().split()))


print(*list(product(A,B)))



'''
from itertools import product
A=[]

n=int(input("Enter your elements:"))

for i in range(0,n):
      ele=int(input())
      A.append(ele)

print(A)


B=[]
n1=int(input("Enter your elements:"))

for i in range(0,n):
      ele=int(input())
      B.append(ele)
print(B)


print(list(product(A,B)))
'''