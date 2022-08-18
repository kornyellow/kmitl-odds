import math

print("*** New Range ***")
print("Enter Input : ", end="")
n = list(map(float, input().split(" ")))

l = []
if len(n) == 3:
    start = n[0]
    end = n[1]
    off = n[2]
    while (start < end):
        l.append(round(start, 3))
        start += n[2]
elif len(n) == 2:
    off = n[0] % 1
    l = list(map(float, range(math.floor(n[0]), math.ceil(n[1]), 1)))
    for e in range(len(l)): l[e] += off
else:
    l = list(map(float, range(0, math.ceil(n[0]), 1)))
r = str(l).replace("\'", "")
r = r.replace("[", "(").replace("]", ")")
print(r)
