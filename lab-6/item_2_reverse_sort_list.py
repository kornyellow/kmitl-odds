def main():
    l = input("Enter your List : ").split(",")
    print("List after Sorted : ", end="")
    print(reverse_sort(l))

def find_max_idx(l, mx=0, i=0):
    if i == len(l):
        return mx
    return find_max_idx(l, i if int(l[i]) > int(l[mx]) else mx, i+1)

def reverse_sort(l, r=[]):
    if len(l) == 0:
        return r
    r.append(int(l.pop(find_max_idx(l))))
    return reverse_sort(l, r)

if __name__ == "__main__":
    main()
