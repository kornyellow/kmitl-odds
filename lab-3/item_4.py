ip = input("Enter Input : ").split(",")

a = []
for l in ip:
    if l == "B":
        print(len(a))
    else:
        h = int(l.split(" ")[1])
        while True:
            if len(a) == 0:
                break
            if h >= a[-1]:
                a.pop()
            else:
                break
        a.append(h)
