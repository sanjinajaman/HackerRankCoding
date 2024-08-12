#!/bin/python3

import string

# Complete the solve function below.
def solve(s):
    y = ''
    for i in s.split():
        #print(i)
        x=i.capitalize()
        print(x)
        ' '.join(x)
    return y
   #return ' '.join(i.capitalize()  for i in s.split(' '))
    return string.capwords(s,' ')


s = input()
result = solve(s)
print(result)





