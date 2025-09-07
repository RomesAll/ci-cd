class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def set_plus(self):
        return self.a + self.b
    

calc = Calc(13,94)
print(calc.a, calc.b)