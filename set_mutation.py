n=int(input())
A=set(map(int,input().split()))
Num_of_op=int(input())

for i in range(0,Num_of_op):
    op_name =input().split()
    #typecas=int(op_name[1])
    new_set = set(map(int, input().split()))

    if op_name[0] =='intersection_update':

        A.intersection_update(new_set)

    elif op_name[0] == 'update':

        A.update(new_set)


    elif op_name[0]=='symmetric_difference_update':

        A.symmetric_difference_update(new_set)

    elif op_name[0]=='difference_update':

        A.difference_update(new_set)




print(sum(A))





#x='intersection_update 10'
# op_name=input().split() #input:inter 10
#
# print(op_name[0]) #inter
# print(op_name[1]) #10


