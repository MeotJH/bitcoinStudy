from FieldElement import FieldElement

a = FieldElement(7,13)
b = FieldElement(12,13)
c = FieldElement(6,13)

print( a+b == c)

d = FieldElement(7,13)
e = FieldElement(2,13)
f = FieldElement(5,13)

print( d - e == f )

aa = FieldElement(3,13)
bb = FieldElement(12,13)
cc = FieldElement(10,13) 

print ( aa * bb == cc )