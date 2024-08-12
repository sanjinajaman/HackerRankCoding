from collections import OrderedDict
N=int(input())
#order_dic=dict()
#Ordered dictionaries are just like regular dictionaries but they remember the order that items were inserted
order_dic= OrderedDict()

for i in range(N):
  key=input().split()
  #print(key)
  k=' '.join(key[:-1])
  #print(k)
  price=int(key[-1])
  #print(price)

  if k in order_dic:
      order_dic[k]=order_dic[k]+price
      #print(order_dic[k])
  else:
      order_dic[k]= price
      #print(order_dic[k])

x=order_dic.items()
for k, price in x :

   print(k,price)



