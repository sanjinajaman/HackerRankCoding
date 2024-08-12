from collections import Counter
x=int(input("Enter number of shoes size: "))  #take  size of shoes


shoes_size_list=list(map(int , input().split()))  #take list  availabe shoe size
Dic =Counter(shoes_size_list)  # counter fuction are counts the same size how many shoes
#print(shoes_size_list)

n=int(input("Enter number of customer"))  #enter number of  customer who buy a shoe
p=0
for i in range(n):
      size,price=map(int,input().split())

      if    Dic[size]:
            Dic[size]-=1
            p=p+price

print(p)


'''input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

output:200
'''