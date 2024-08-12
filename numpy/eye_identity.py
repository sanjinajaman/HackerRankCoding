import numpy
numpy.set_printoptions(legacy="1.13")

N,M=map(int, input().split())

if N==M:
    print(numpy.identity(N))

else:
  print(numpy.eye(N,M))


