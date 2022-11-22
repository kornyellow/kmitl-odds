def minimum_weight(box, num):
    left, right = max(box), sum(box)
    while left < right:
        mid = (left + right) / 2
        want = 1
        curr = 0
        for b in box:
            if curr + b > mid:
                want += 1
                curr = 0
            curr += b
        if want > num:
            left = mid + 1
        else:
            right = mid
    return int(left)

def main():
    box, num = input("Enter Input : ").split("/")
    box = list(map(int, box.split()))
    num = int(num)

    print("Minimum weigth for " + str(num) + " box(es) = " + str(minimum_weight(box, num)))

if __name__ == "__main__":
    main()
