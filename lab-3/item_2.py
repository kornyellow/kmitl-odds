def parenCheck(p):
    stack = []
    opn = "([{"
    cls = ")]}"
    for e in p:
        if e in opn:
            stack.append(e)
        elif e in cls:
            if len(stack) == 0:
                return 1, []
            a = stack[-1]
            if cls.index(e) == opn.index(a):
                stack.pop()
            else:
                return 0, []
    if len(stack) == 0:
        return -1, []
    return 2, stack

ip = input("Enter expresion : ")

e, l = parenCheck(ip)
if e == -1:
    print(ip, "MATCH")
elif e == 0:
    print(ip, "Unmatch open-close")
elif e == 1:
    print(ip, "close paren excess")
else:
    print(ip, "open paren excess  ", len(l), ":", "".join(l))
