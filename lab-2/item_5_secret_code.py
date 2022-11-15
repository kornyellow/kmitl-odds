def main():
    code = input("Enter secret code : ")
    print(bon(code))

def bon(w):
    l = {}
    for e in w:
        if e not in l:
            l[e] = 0
        l[e] += 1
    v_max = 0
    k_max = None
    for k in l:
        if l[k] > v_max:
            v_max = l[k]
            k_max = k
    v = (ord(k_max)-ord('a')+1)*2
    return v*2

if __name__ == "__main__":
    main()
