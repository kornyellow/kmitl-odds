def main():
    n = int(input("Enter Input : "))
    if n == 0:
        print("Not Draw!")
    else:
        print(staircase(n))

def sign(x):
    if x == 0:
        return 0
    return 1 if x > 0 else -1

def append_repeat(times, item, i=0):
    if i == times:
        return []
    return [item] + append_repeat(times, item, i+1)

def staircase(m, i=0):
    if i == 0:
        i = 1 if m > 0 else abs(m)

    ret = []
    ret += append_repeat(abs(m)-i, "_")
    ret += append_repeat(i, "#")

    if i == (m if m > 0 else 1):
        return "".join(ret)
    ret.append("\n")
    return "".join(ret) + staircase(m, i+sign(m))

if __name__ == "__main__":
    main()
