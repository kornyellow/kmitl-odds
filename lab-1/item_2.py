print("*** multiplication or sum ***")
print("Enter num1 num2 : ", end="")
num1, num2 = list(map(int, input().split(" ")))
print("The result is %d" % ((num1*num2) if num1*num2 <= 1000 else (num1+num2)))
