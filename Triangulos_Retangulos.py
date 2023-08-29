import math

pow = math.pow

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        if pow(self.b, 2) + pow(self.c, 2) == pow(self.a, 2) or pow(self.a, 2) + pow(self.c, 2) == pow(self.b, 2) or pow(self.a, 2) + pow(self.b, 2) == pow(self.c, 2):
            return True
        else:
            return False
