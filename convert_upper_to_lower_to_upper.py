'''s=input()
x=s.upper()
print(x)
y=s.lower()
print(y)
z=s.swapcase()
print(z)
#print((s))'''



def swap_case(s):
    x = ""
    for i in s:
        if i.isupper(): #check is upper case or not
           c=i.lower()  #convert is lower case store result c
        else:
            c=i.upper() #convert is upper case store result c
        x+="".join(c)  #join total result this empty space
    return x

s=input()
z=swap_case(s)
print(z)