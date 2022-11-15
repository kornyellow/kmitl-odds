def main():
    inp = list(map(int, input("Enter Input : ").split()))
    lst, logs = bubble_sort(inp)

    for i in range(len(logs)):
        if i != len(logs) - 1:
            print("%d step :" % (i + 1), logs[i])
        else:
            print("last step :", logs[i])

def bubble_sort(lst):
    logs = []
    size = len(lst) - 1
    for _ in range(size):
        move = None
        for i in range(size):
            if lst[i] > lst[i + 1]:
                move = temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
        logs.append(str(lst) + " move[" + str(move) + "]")
        if not move:
            break
    return lst, logs

if __name__ == "__main__":
    main()
