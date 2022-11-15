def main():
    inp = list(map(int, input("Enter Input : ").split()))
    lst, logs = selection_sort(inp)

    if logs != []:
        print("\n".join(logs))
    print(lst)

def selection_sort(lst):
    logs = []
    size = len(lst)
    for t in range(size - 1):
        swap = 0
        for i in range(size - t):
            if lst[i] > lst[swap]:
                swap = i
            if i == size - t - 1 and i != swap:
                temp = lst[i]
                lst[i] = lst[swap]
                lst[swap] = temp
                logs.append("swap " + str(lst[swap]) + " <-> " + str(lst[i]) + " : " + str(lst))
    return lst, logs

if __name__ == "__main__":
    main()
