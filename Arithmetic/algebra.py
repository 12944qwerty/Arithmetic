import math

class Algebra(object):
    def zeros(self,a,b,c):
        """Gets the zeros of a quadratic function. Args are A, B, and C in form 'Ax^2 + Bx + C'."""
        first = (-b + math.sqrt(b ** 2 - (4*a*c)))/(2 * a)
        second = (-b - math.sqrt(b ** 2 - (4*a*c)))/(2* a)
        return str(first) + ', ' + str(second)
