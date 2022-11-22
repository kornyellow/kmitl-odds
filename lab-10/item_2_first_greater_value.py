def main():
    lst, keys = input("Enter Input : ").split("/")
    lst = list(map(int, lst.split()))
    keys = list(map(int, keys.split()))
    lst = bubble_sort(lst)
    for key in keys:
        res = find_least_min(lst, key, 0, len(lst) - 1)
        if res != 1000000:
            print(res)
        else:
            print("No First Greater Value")

def find_least_min(lst, key, left, right, least=1000000):
    if left != right - 1:
        pivot = left + ((right - left) // 2);
        if key >= lst[pivot]:
            left = pivot
            if lst[pivot] < least and lst[pivot] > key:
                least = lst[pivot]
        elif key < lst[pivot]:
            right = pivot
            if lst[pivot] < least and lst[pivot] > key:
                least = lst[pivot]
        return find_least_min(lst, key, left, right, least)
    return least

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

if __name__ == "__main__":
    main()
