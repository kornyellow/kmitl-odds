def main():
    l = input("Enter Input : ").split()
    print("Min : %d" % find_min(l))

def find_min(l, mn=99999, i=0):
    if i == len(l) -1:
        return mn
    return find_min(l, int(l[i]) if int(l[i]) < mn else mn, i+1)

if __name__ == "__main__":
    main()
