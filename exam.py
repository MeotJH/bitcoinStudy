from FieldElement import FieldElement

a = FieldElement(7,13)
b = FieldElement(12,13)
c = FieldElement(6,13)

print("1",a+b == c)

d = FieldElement(7,13)
e = FieldElement(2,13)
f = FieldElement(5,13)

print( "2",d - e == f )

aa = FieldElement(3,13)
bb = FieldElement(12,13)
cc = FieldElement(10,13) 

print ( "3",aa * bb == cc )

dd = FieldElement(3, 13)
ee = FieldElement(1, 13)

print ( "4",dd ** 3 == ee)

aaa = FieldElement(3,31)
bbb = FieldElement(24,31)
ccc = FieldElement(4, 31)


print ( "5",aaa/bbb == ccc )