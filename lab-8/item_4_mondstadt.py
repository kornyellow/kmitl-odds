def main():
    raw_input = input("Enter Input : ")
    numbers, constraint = raw_input.split("/")
    numbers = list(map(int, numbers.split()))
    constraint = constraint.split(",")

    constraint_pair = []
    for e in constraint:
        constraint_pair.append(list(map(int, e.split())))

    attack_sum = 0
    for num in numbers:
        attack_sum += num
    print(attack_sum)

    for const in constraint_pair:
        attack_a = get_attack_sum(numbers, const[0])
        attack_b = get_attack_sum(numbers, const[1])
        if attack_a > attack_b:
            print("%d>%d" % (const[0], const[1]))
        if attack_a < attack_b:
            print("%d<%d" % (const[0], const[1]))
        if attack_a == attack_b:
            print("%d=%d" % (const[0], const[1]))

def get_attack_sum(attack_list, n):
    res = 0
    if (2 * n + 1) < len(attack_list):
        res += attack_list[2 * n + 1]
    if (2 * n + 2) < len(attack_list):
        res += attack_list[2 * n + 2]
    return attack_list[n] + res

if __name__ == "__main__":
    main()
