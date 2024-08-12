from itertools import combinations
N=int(input())
n=list(input().split())
K=int(input())
x=list(combinations(n,K))
print(x)
c=0

for i in x:
    #print(i)
    if 'a' in i:
        c=c+1
print(c/len(x))





