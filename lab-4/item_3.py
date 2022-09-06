class Queue:
    def __init__(self, lst=None):
        self.items = lst
        if lst is None:
            self.items = []

    def enqueue(self, e):
        self.items.append(e)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0


def main():
    inp, cmds = tuple(input("Enter Input : ").split("/"))

    book = Queue(inp.split())
    for cmd in cmds.split(","):
        if cmd == "D":
            book.dequeue()
        else:
            e = cmd.split(" ")[1]
            book.enqueue(e)

    seen = []
    is_dup = False
    for b in book.items:
        if b in seen:
            is_dup = True
            break
        else:
            seen.append(b)

    if not is_dup:
        print("NO Duplicate")
    else:
        print("Duplicate")

if __name__ == "__main__":
    main()
