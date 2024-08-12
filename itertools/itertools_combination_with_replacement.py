from itertools import combinations_with_replacement



s=input().split()
string=sorted(s[0])
k=int(s[1])
# print(string)
# print(k)

x=list(combinations_with_replacement(string,k))
#print(x)
for j in x:
    #print(j)
    print(''.join(j))
