n=int(input())
s1=set(map(int,input().split()))
b=int(input())
s2=set(map(int,input().split()))

union=s1.union(s2)
print(len(union))

