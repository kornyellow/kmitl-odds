class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return "".join(self.items)

    def push(self, e):
        self.items.append(e)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0


def paren_check(p):
    s = Stack()
    opn = "([{"
    cls = ")]}"
    for e in p:
        if e in opn:
            s.push(e)
        elif e in cls:
            if s.is_empty():
                return "close paren excess"
            if cls.index(e) != opn.index(s.peek()):
                return "Unmatch open-close"
            s.pop()

    if s.is_empty():
        return "MATCH"
    return f"open paren excess   {s.size()} : {str(s)}"

def main():
    ip = input("Enter expresion : ")
    print(ip, paren_check(ip))

if __name__ == "__main__":
    main()
