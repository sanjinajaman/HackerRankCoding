#it's work pypy3
n=int(input())
t=tuple(map(int,input().split(' ')))

print(hash(t))

'''input:2
         1 2'''

'''here has some problem my expected result is 3550055125485641917
but it gives  :-3550055125485641917'''
