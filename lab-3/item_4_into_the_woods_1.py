def main():
    inp = input("Enter Input : ").split(",")

    s = Stack()
    for e in inp:
        if e == "B":
            print(s.size())
        else:
            h = int(e.split(" ")[1])
            while True:
                if s.is_empty():
                    break
                if h >= s.peek():
                    s.pop()
                else:
                    break
            s.push(h)

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

if __name__ == "__main__":
    main()
