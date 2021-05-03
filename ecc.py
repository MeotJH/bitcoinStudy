class FieldElement:
    
    def __init__(self, num, prime):
        if num >= prime or num < 0 :
            error = 'num {} not in field range 0 to {}'.format(
                num, prime -1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)   
        

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num )%self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num - other.num)%self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num * other.num)%self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        n = exponent % ( self.prime-1 )
        num = pow(self.num , n , self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        num = self.num*pow(other.num,self.prime-2,self.prime)%self.prime
        return self.__class__(num, self.prime)
    
class Point:

    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None:
            return

        if self.y**2 != self.x**3 + a*x + b:
            raise ValueError('({},{}) is not on the curve'.format(x,y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        if self.x is None:
            return 'Point(infinity)'
        elif isinstance(self.x, FieldElement):
            return 'Point({},{})_{}_{} FieldElement({})'.format(
                self.x.num, self.y.num, self.a.num, self.b.num, self.x.prime)
        else:
            return 'Point({},{})_{}_{}'.format(self.x, self.y, self.a, self.b)

    def __add__(self, other):
        
        if self.a != other.a or self.b != other.b:
            raise TypeError('포인트 {},{}는 같은 커브에 있지 않다.'.format(self,other))

        if self.x is None:
            return other
        if other.x is None:
            return self

        if self.x == other.x and self.y != other.y:
            return self.__class__(None,None,self.a,self.b)

        if self.x != other.x:
            
            inclination = (other.y - self.y )/( other.x - self.x)
            x = inclination**2 - self.x - other.x
            y = inclination*(self.x - x ) - self.y
            return self.__class__( x, y, self.a, self.b)

        if self.x == other.x:

            inclination = (3*(self.x**2)+self.a)/(2*self.y)
            print(inclination)
            x = inclination**2 - 2*self.x
            y = inclination*(self.x - x) - self.y
            return self.__class__( x, y, self.a, self.b)

        if self == other and self.y == 0 * self.x:
            return self.__class__(None, None, self.a, self.b)

# class ECCTest(TestCase):

#     def test_on_curve(self):
#         prime = 223
#         a = FieldElement(0, prime)
#         b = FieldElement(7, prime)
#         valid_points = ((192, 105), (17, 56), (1, 193))
#         invalid_points = ((200, 119), (42, 99))
#         for x_raw, y_raw in valid_points:
#             x = FieldElement(x_raw, prime)
#             y = FieldElement(y_raw, prime)
#             Point(x, y, a, b)  # <1>
#         for x_raw, y_raw in invalid_points:
#             x = FieldElement(x_raw, prime)
#             y = FieldElement(y_raw, prime)
#             with self.assertRaises(ValueError):
#                 Point(x, y, a, b)  # <1


