from collections import OrderedDict
N=int(input())

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
      print(order_dic[k])
  else:
      order_dic[k]= price
      print(order_dic[k])
for k, price in order_dic.items():

   print(k,price)



