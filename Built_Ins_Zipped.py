N, X=map(int, input().split())
List=[]
for i in range(X):
    ls=list(input().split())
    ls=[float(j) for j in ls]
    List.append(ls)



#The * syntax is useful when you have a collection of values (in this case, a list)
# that you want to print without explicitly specifying each element as a separate argument.


for k in zip(*List):
    #print(k)
    print(sum(k)/len(k))