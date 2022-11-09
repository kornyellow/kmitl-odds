def insertion_sort(lst, temp=[], logs=[]):
    if len(lst) != 0:
        key = lst.pop(0)
        if len(temp) == 0:
            temp.append(key)
        else:
            i = 0
            for _ in range(len(temp)):
                if temp[i] < key:
                    i += 1
            temp.insert(i, key)

            # Check if original list contain any items, if not make it an empty string
            lst_str = " " + str(lst) if len(lst) != 0 else ""
            logs.append("insert " + str(key) + " at index " + str(i) + \
                        " : " + str(temp) + lst_str)
        return insertion_sort(lst, temp)
    return temp, logs

if __name__ == "__main__":
    inp = list(map(int, input("Enter Input : ").split()))

    lst, logs = insertion_sort(inp)

    if logs != []:
        print("\n".join(logs))
    print("sorted")
    print(lst)
