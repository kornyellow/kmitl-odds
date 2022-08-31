def find_min(l, mn=99999, i=0):
    if i == len(l) -1:
        return mn
    return findMin(l, int(l[i]) if int(l[i]) < mn else mn, i+1)

l = input("Enter Input : ").split()
print("Min : %d" % find_min(l))

