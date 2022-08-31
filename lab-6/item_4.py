def display(i, a, b, c):
    if i == 0:
        return
    if i < len(a):
        print(a[i], end="  ")
    else:
        print("|", end="  ")
    if i < len(b):
        print(b[i], end="  ")
    else:
        print("|", end="  ")
    if i < len(c):
        print(c[i])
    else:
        print("|")
    i -= 1
    display(i, a, b, c)

def move(n, m, a, b, c):
    if n == 1:
        if a[0] == "A" and c[0] == "B":
            b.append(a.pop())
        elif a[0] == "B" and c[0] == "C":
            c.append(b.pop())
        elif a[0] == "A" and c[0] == "C":
            c.append(a.pop())
        elif a[0] == "C" and c[0] == "B":
            b.append(c.pop())
        elif a[0] == "B" and c[0] == "A":
            a.append(b.pop())
        elif a[0] == "C" and c[0] == "A":
            a.append(c.pop())
        print("move 1 from  %s to %s" % (a[0], c[0]))
        print("|  |  |")
        display(m, a, b, c)

        b[0], c[0] = c[0], b[0]
        return a, b, c
    else:
        bb, cc = b.copy(), c.copy()
        bb[0], cc[0] = c[0], b[0]
        a, b, c = move(n-1, m, a, bb, cc)

        if a[0] == "A" and c[0] == "B":
            b.append(a.pop())
        elif a[0] == "B" and c[0] == "C":
            c.append(b.pop())
        elif a[0] == "A" and c[0] == "C":
            c.append(a.pop())
        elif a[0] == "C" and c[0] == "B":
            b.append(c.pop())
        elif a[0] == "B" and c[0] == "A":
            a.append(b.pop())
        elif a[0] == "C" and c[0] == "A":
            a.append(c.pop())
        print("move %d from  %s to %s" % (n, a[0], c[0]))
        print("|  |  |")
        display(m, a, b, c)

        aa, bb = a.copy(), b.copy()
        aa[0], bb[0] = b[0], a[0]
        a, b, c = move(n-1, m, aa, bb, c)

        a[0], c[0] = c[0], a[0]
        return a, b, c

n = int(input("Enter Input : "))
a = ["A"]
b = ["B"]
c = ["C"]
a += list(range(n, 0, -1))

print("|  |  |")
display(n, a, b, c)

move(n, n, a, b, c)
