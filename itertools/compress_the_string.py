import itertools
s=input()

x=itertools.groupby(s)
#print(x)

for key , grp in x:
    print((len(list(grp)), int(key)), end=" ")