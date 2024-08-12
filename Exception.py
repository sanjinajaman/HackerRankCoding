#run this program pypy3
T=int(input()) #enter the number of test cases

for i in range(0,T):
    try:
        a,b=map(int, input().split())
        print(a//b) #For integer division in Python 3 use //
    except Exception as e:
           print ( "Error Code:",e)

