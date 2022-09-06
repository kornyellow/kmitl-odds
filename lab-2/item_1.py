class Calculator:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.val + other.val

    def __sub__(self, other):
        return self.val - other.val

    def __mul__(self, other):
        return self.val * other.val

    def __truediv__(self, other):
        return self.val / other.val


def main():
    x,y = input("Enter num1 num2 : ").split(",")
    x,y = Calculator(int(x)), Calculator(int(y))
    print(x+y, x-y, x*y, x/y, sep="\n")

if __name__ == "__main__":
    main()
