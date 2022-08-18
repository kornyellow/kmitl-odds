ip = input("Enter Input : ").split(",")

a = []
for l in ip:
    if l == "B":
        c = 0
        m = 0
        b = a.copy()
        b.reverse()
        for e in b:
            if e > m:
                m = e
                c += 1
        print(c)
    elif l == "S":
        if len(a) != 0:
            for i in range(len(a)):
                if a[i] % 2 == 1:
                    a[i] += 2
                else:
                    a[i] = max(1, a[i]-1)
    else:
        h = int(l.split(" ")[1])
        a.append(h)
