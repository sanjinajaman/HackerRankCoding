import math

AB=int(input())
BC=int(input())


thita=(math.atan(AB/BC))

degree=round(math.degrees(thita))

print(degree, chr(176),sep="")