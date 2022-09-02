def sign(x):
    if x == 0:
        return 0
    return 1 if x > 0 else -1

def staircase(m, i=0):
    if i == 0:
        i = 1 if m > 0 else abs(m)

    ret = []
    for _ in range(abs(m)-i):
        ret.append("_")
    for _ in range(i):
        ret.append("#")

    if i == (m if m > 0 else 1):
        return "".join(ret)
    ret.append("\n")
    return "".join(ret) + staircase(m, i+sign(m))

n = int(input("Enter Input : "))
if n == 0:
    print("Not Draw!")
else:
    print(staircase(n))
