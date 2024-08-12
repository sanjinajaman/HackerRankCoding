a,b=map(int,input().split())
#s=input() #for middle value=====s=WELCOME
s1='.|.'
s2='WELCOME'
#upper level
for i in range(a//2):
    #print(a//2)
    #print(i)
    print((s1*((i*2)+1)).center(b,'-')) #4times
#print(a//2)

#middle level
print(s2.center(b,'-')) #5th times
#lower level
#print(a//2-1)
for i in range(a//2-1,-1,-1): #(4-1=3)
    print(i)
    print((s1*((i*2)+1)).center(b,'-'))

print(a//2-1)

