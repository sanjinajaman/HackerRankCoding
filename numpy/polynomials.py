import numpy

P=list(map(float, input().split()))
x=int(input())
'''
This line uses the NumPy function polyval to evaluate the polynomial defined by the coefficients in the list P at the value x.
The result is stored in the variable Poly.
'''
Poly=numpy.polyval(P, x)
print(Poly)
# print(P)

'''
the polynomial 1*x^2 + 2*x + 3 is evaluated at x = 4, resulting in the output 27.0.

'''