class Stack:
    def __init__(self, l=None):
        if l == None:
            self.items = []
        else:
            self.items = l

    def push(self, e):
        self.items.append(e)

    def peek(self, i=-1):
        return self.items[i]

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return "".join(self.items)


def checkprio(e):
    if e in "+-":
        return 1
    if e in "*/":
        return 2
    if e in "^":
        return 3

def get_close_brace_index(l, i):
    stack = Stack()
    stack.push(l[i])
    i += 1
    while True:
        if l[i] == "(":
            stack.push(l[i])
        elif l[i] == ")":
            stack.pop()
            if stack.isEmpty():
                return i
        i += 1

def postfix(l):
    stack = Stack()
    ans = []
    i = 0
    n = len(l)
    while i < n:
        e = l[i]
        if e in "+-*/^":
            while not stack.isEmpty():
                cp = checkprio(e)
                cp_s = checkprio(stack.peek())
                if cp_s >= cp:
                    ans.append(stack.pop())
                else:
                    break
            stack.push(e)
        elif e in "(":
            b_i = get_close_brace_index(l, i)
            ip = l[i+1:b_i]
            ans.append(postfix(ip))
            i += len(ip)+1
        else:
            ans.append(e)
        i += 1
    while not stack.isEmpty():
        ans.append(stack.pop())
    return "".join(ans)

def main():
    ip = input("Enter Infix : ")
    print("Postfix", ":", postfix(ip))

if __name__ == "__main__":
    main()
