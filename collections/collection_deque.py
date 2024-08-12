from collections import deque


d=deque()
N=int(input())

#print(d)
for i in range(N):
    N_ele = input()

    if N_ele =="pop":
       d.pop()
    elif N_ele=="popleft":
        d.popleft()
    else:
        command , value=N_ele.split()
        # print(command, value)
        # print(command)
        # print(value)
        v=int(value)
        if command=="append":
            d.append(v)
        elif command=="appendleft":
            d.appendleft(v)
print(*d)


