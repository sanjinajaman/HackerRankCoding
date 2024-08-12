x=int(input())
a=[]
for i in range(x):
    a.append(input())

b=set(a)

print(len(b))

x=int(input())
a=set()
for i in range(x):
    a.add(input())
print(len(a))
