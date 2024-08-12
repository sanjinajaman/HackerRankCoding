'''
Fibonacci

The Fibonacci sequence is the series of numbers where each number is the sum of the two preceding numbers. For example,

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, …

Mathematically we can describe this as:

xn= xn-1 + xn-2'''


cube = lambda x: pow(x,3)

def fibonacci(n):
    lis=[0,1]
    for i in range(2,n):
        lis.append(lis[i-2]+ lis[i-1])

        # print(lis)
    return (lis[0:n])


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
