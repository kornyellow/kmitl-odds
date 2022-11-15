def main():
    print("*** Fun with Drawing ***")
    print("Enter input : ", end="")
    n = int(input())

    r = ((n - 1) * 4) + 1
    m = r / 2
    for i in range(r):
        for j in range(r):
            case1 = i % 2 == 0 and (j >= i and j <= r - i - 1) and i <= m + 1
            case2 = i % 2 == 0 and (j <= i and j >= r - i - 1) and i > m + 1
            case3 = j % 2 == 0 and (i >= j and i <= r - j - 1) and j <= m + 1
            case4 = j % 2 == 0 and (i <= j and i >= r - j - 1) and j > m + 1
            if case1 or case2 or case3 or case4:
                print("#", end="")
            else:
                print(".", end="")
        print("")

if __name__ == "__main__":
    main()
