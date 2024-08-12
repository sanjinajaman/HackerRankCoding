# N=int(input())
#
# List=list(input().split())
#
# positive=all([int(i)>0 for i in List])
# pal=any([st== st[::-1] for st in List])
#
# print(positive and pal)


N , ele=int(input()), input().split()
print(all([int(i)>0 for i in ele]) and any([st== st[::-1] for st in ele]))


