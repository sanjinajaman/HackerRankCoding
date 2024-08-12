'''def average(array):
      array = set(array)
      return sum(array)/len(array)

      # sum=0
      # for i in range(len(array)):
      #       sum=sum+array[i]
      #
      # x=(sum/len(array))
      # print(x)


#n=int(input())

arr=list(map(int , input().split()))

# for i in range (0,n):
#     ele=input().split()
#     arr.append(ele)
result=average(arr)
print(result)

#print(arr)'''

'''10                                         
161 182 161 154 176 170 167 171 170 174 '''


def average(array):
      array=set(array)
      return sum(array)/len(array)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)