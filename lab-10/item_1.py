def bubble_sort(lst):
    size = len(lst) - 1
    for _ in range(size):
        move = None
        for i in range(size):
            if lst[i] > lst[i + 1]:
                move = temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
        if not move:
            break
    return lst

def binary_search(left, right, lst, key):
    while True:
        pivot = left + ((right - left) // 2);
        if key > lst[pivot]:
            left = pivot
        elif key < lst[pivot]:
            right = pivot
        else:
            return True
        if left == right - 1:
            break
    return False

if __name__ == "__main__":
    lst, key = input("Enter Input : ").split("/")
    key = int(key)
    lst = bubble_sort(list(map(int, lst.split())))
    print(binary_search(0, len(lst) - 1, lst, key))
