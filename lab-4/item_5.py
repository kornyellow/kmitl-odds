def process_candy(candy):
    item = []
    last = -1
    exp = 0
    while True:
        old_candy = candy.copy()
        for i in range(len(candy)):
            piece = candy[i]
            matches = 1
            for j in range(1, 3):
                if i+j >= len(candy):
                    break
                elif candy[i+j] != piece:
                    break
                else:
                    matches += 1
            if matches == 3:
                if i < last:
                    item.insert(0, piece)
                else:
                    item.append(piece)
                last = i
                left = candy[0:i]
                right = candy[i+3:]
                candy = left+right
                exp += 1
                break
        if candy == old_candy:
            break
    return candy, item, exp

def use_item(candy, item):
    failed = 0
    i = 0
    while i < len(candy):
        piece = candy[i]
        matches = 1
        for j in range(1, 3):
            if i+j >= len(candy):
                break
            elif candy[i+j] != piece:
                break
            else:
                matches += 1
        if matches == 3 and len(item) != 0:
            a = item.pop()
            candy.insert(i+2, a)
            i += 2
            if a == piece:
                failed += 1
        elif len(item) == 0:
            break
        i += 1
    return candy, failed

normal, mirror = input("Enter Input (Normal, Mirror) : ").split(" ")
normal = [*normal]
mirror = [*mirror]

mirror, mirror_item, mirror_exp = process_candy(mirror)
normal, failed = use_item(normal, mirror_item)
normal, normal_item, normal_exp = process_candy(normal)
normal.reverse()

print("NORMAL :")
print(len(normal))
if len(normal) == 0:
    print("Empty")
else:
    print("".join(normal))
print(normal_exp-failed, "Explosive(s) ! ! ! (NORMAL)")
if failed > 0:
    print("Failed Interrupted %d Bomb(s)" % (failed))

print("------------MIRROR------------")

print(": RORRIM")
print(len(mirror))
if len(mirror) == 0:
    print("ytpmE")
else:
    print("".join(mirror))
print("(RORRIM) ! ! ! (s)evisolpxE", mirror_exp)
