from itertools import permutations

# size, price = map(int, input().split())
s,k=input().split(" ")

p=permutations(sorted(s),int(k) )
for i in list(p):
  #print(tuple(i))
  print(''.join(i))

# print(s)
# print(k)

'''
input :ah 2
output:
ah
ha

'''