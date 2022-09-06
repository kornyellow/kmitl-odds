def main():
    print("*** Fun with countdown ***")
    print("Enter List : ", end="")
    l = list(map(int, input().split(" ")))

    p = -1
    a = []
    r = []
    for e in l:
        if p == -1:
            p = e
            a.append(e)
            if p == 1:
                r.append(a)
                a = []
                p = -1
        elif e == 1:
            a.append(e)
            r.append(a)
            a = []
            p = -1
        elif p-1 == e:
            a.append(e)
            p = e
        else:
            a = []
            a.append(e)
            p = e
    o = []
    o.append(len(r))
    o.append(r)
    print(o)

if __name__ == "__main__":
    main()
