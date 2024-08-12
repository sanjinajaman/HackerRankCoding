from collections import namedtuple
n=int(input())

#This line dynamically creates a namedtuple class named "data" with fields specified by the user input. The user is expected to provide space-separated field names.
data = namedtuple("data",input())

#print("data",data)
marks_lst=[]

#* this is accept all the argument

'''
This loop iterates n times, taking user input for each instance, splitting the input into values,
creating a namedtuple instance using those values, and extracting the value of the "MARKS" field. 
The extracted mark is then converted to an integer and appended to the marks_lst.

'''
for i in range(n):

    marks=int(data(*input().split()).MARKS)

    marks_lst.append(marks)
print(sum(marks_lst)/n)


n=int(input())
data = namedtuple("data",input())
marks_lst=[]
print( sum( int(data(*input().split()).MARKS)) for i  in range(n) )



