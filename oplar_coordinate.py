


#import cmath for complex number operations
import cmath

z=complex((input().strip()))
print(z)

'''The cmath.polar() method converts a complex number to polar coordinates. It returns a tuple of modulus and phase.

In polar coordinates, a complex number is defined by modulus r and phase angle phi.'''
#find the polar coordinates of complex number
res=cmath.polar(z)
print(res)# result e duita value store hoise as e touple er value duitar postion 1st index [0] and second index[1]
print(res[0])
print(res[1])