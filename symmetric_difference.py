M=int(input())
a=set(map(int, input().split()))
N=int(input())
b=set(map(int, input().split()))

result=a.symmetric_difference(b)
print(*sorted(result),sep="\n")
'''
Unpacking a Function Using the Positional Argument
This technique is extremely helpful when we have to print information in a raw format
that is without any brackets and commas. This prefix asterisk can help you in 
unpacking them because many programmers attempt to remove the bracket and comma by using a convolution of functions.
'''