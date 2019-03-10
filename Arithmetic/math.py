class Math(object):
    def multiply(self,x,y):
        return x * y

    def add(self,x,y):
        return x + y

    def divide(self,x,y):
        return x / y

    def subtract(self,x,y):
        return x - y

    def power(self,x,y):
        return x ** y

    def root(self,x,y):
        """Args: Numb, Root. Number is the number in radical. Root is like cuberoot or sqrt but as int."""
        i = 0
        while i < x:
            if i ** y == x:
                return int(i)
                break
            i += 1

class Algebra(object):
    def zeros(self,a,b,c):
        """Gets the zeros of a quadratic function. Args are A, B, and C in form 'Ax^2 + Bx + C'."""
        first = (-b + math.root(b ** 2 - (4*a*c),2))/(2 * a)
        second = (-b - math.root(b ** 2 - (4*a*c),2))/(2* a)
        return str(first) + ', ' + str(second)
