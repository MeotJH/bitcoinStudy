from ecc import Point, FieldElement

a = FieldElement(0,223)
b = FieldElement(7,223)
x = FieldElement(192,223)
y = FieldElement(105,223)

p1 = Point(x, y, a, b)
print(p1)

