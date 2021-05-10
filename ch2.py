import ecc 
#from helper import run

prime = 223
a = ecc.FieldElement(0, prime)
b = ecc.FieldElement(7, prime)
x = ecc.FieldElement(47, prime)
y = ecc.FieldElement(71, prime)
p = ecc.Point(x, y, a, b)
for s in range(1,21):
        result = s*p
        print('{}*(47,71)=({},{})'.format(s,result.x.num,result.y.num)) 