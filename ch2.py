import ecc 
#from helper import run

prime = 223
a = ecc.FieldElement(0,prime)
b = ecc.FieldElement(7,prime)
x1 = ecc.FieldElement(192, prime)
y1 = ecc.FieldElement(105, prime)
x2 = ecc.FieldElement(17, prime)
y2 = ecc.FieldElement(56, prime)
p1 = ecc.Point(x1, y1, a, b)
p2 = ecc.Point(x2, y2, a, b)

print(p1+p2)