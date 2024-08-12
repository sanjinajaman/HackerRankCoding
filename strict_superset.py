'''A=set(input().split())
N=int(input()) #number of other set

for i in range (N):
    s=set(input().split())
    x=A.issuperset(s)
print(x)'''


A=set(input().split())
N=int(input()) #number of other set
count=0
for i in range (N):
    s=set(input().split())
    if A.issuperset(s):
        continue
    else:
        print("False")
        count=1
        break
if count==0:
    print("True")