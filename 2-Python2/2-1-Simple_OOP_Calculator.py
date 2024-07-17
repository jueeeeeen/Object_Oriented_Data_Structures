class Calculator :

    def __init__(self, value):
        self.value = value

    def __add__(self, a):
        return self.value + a.value

    def __sub__(self, a):
        return self.value - a.value

    def __mul__(self, a):
        return self.value * a.value

    def __truediv__(self, a):
        return self.value / a.value

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")