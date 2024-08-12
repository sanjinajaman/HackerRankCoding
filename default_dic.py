from collections import defaultdict
A=defaultdict(list) #We can pass a list class as the default_factory argument, and it will create a defaultdict with the values that are set in list format.


n , m=map(int,input().split())
for i in range(1,n+1):
      ele=input()  #take a input for key
      A[ele].append(i)


for i in range(m):
    ele2=input()
    if ele2 in A:
        print(A[ele2],sep=" ")
    else:
        print(-1)




