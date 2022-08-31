def pow(n, i):
    if i == 0:
        return 1
    if i == 1:
        return n
    return n * pow(n, i-1)

def generate_binary(m, i):
    if m == 0:
        return ""

    r = generate_binary(m-1, i // 2)
    return r + str(i % 2)

def print_multiple(m, n):
    if m == 0:
        return
    print(generate_binary(n, m))
    print_multiple(m-1, n)

n = int(input("Enter Number : "))
if n > 0:
    m = pow(2, n)
    print_multiple(m, n)
elif n == 0:
    print("0")
else:
    print("Only Positive & Zero Number ! ! !")
