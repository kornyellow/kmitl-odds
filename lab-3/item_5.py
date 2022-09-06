class Stack:
    def __init__(self):
        self.items = []

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


def main():
    inp = input("Enter Input : ").split(",")

    s = Stack()
    for e in inp:
        if e == "B":
            c = 0
            m = 0
            b = s.items.copy()
            b.reverse()
            for x in b:
                if x > m:
                    m = x
                    c += 1
            print(c)
        elif e == "S":
            if not s.is_empty():
                for i in range(s.size()):
                    if s.items[i] % 2 == 1:
                        s.items[i] += 2
                    else:
                        s.items[i] = max(1, s.items[i]-1)
        else:
            h = int(e.split()[1])
            s.push(h)

if __name__ == "__main__":
    main()
