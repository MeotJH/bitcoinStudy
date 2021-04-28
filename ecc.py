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
        # this should be the inverse of the == operator
        raise NotImplementedError

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
        if self.y**2 != self.x**3 + a*x + b:
            raise ValueError('({},{}) is not on the curve'.format(x,y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b