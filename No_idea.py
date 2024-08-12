#1st procedure
num_array_ele,num_set_element=map(int,input().split())
#print(num_array_ele,num_set_element)
a=list(input().split())
#print(a)
A=(input().split())
#print(A)
B=set(input().split())
#print(B)

print(sum((i in A) - (i in B) for i in a))
#2nd procedure

n,m=map(int,input().split())
#print(num_array_ele,num_set_element)
a=list(map(int,input().split()))
#print(a)
A=set(map(int,input().split()))
#print(A)
B=set(map(int,input().split()))
#print(B)

print(sum((i in A) - (i in B) for i in a))

