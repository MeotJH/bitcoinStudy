import ecc 
#from helper import run

gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
p = 2**256 - 2**32 - 977
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
x = ecc.FieldElement(gx, p)
y = ecc.FieldElement(gy, p)
seven = ecc.FieldElement(7, p)
zero = ecc.FieldElement(0, p)
G = ecc.Point(x, y, zero, seven)
print(n*G)