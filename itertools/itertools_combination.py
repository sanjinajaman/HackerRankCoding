from itertools import combinations

s=input().split()
string=sorted(s[0])
k=int(s[1])
# print(string)
# print(k)
for i in range(1, k+1):
    x=list(combinations(string,i))
    #print(x)
    for j in x:
        #print(j)

        print(''.join(j))
