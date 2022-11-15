def main():
    p, t = tuple(input("Enter people and time : ").split())

    q = Queue([*p])
    c1 = Queue()
    c2 = Queue()

    for i in range(int(t)):
        if i % 3 == 0:
            c1.dequeue()
        if (i-7) % 2 == 0:
            c2.dequeue()

        if c1.size() < 5:
            c1.enqueue(q.dequeue())
        else:
            c2.enqueue(q.dequeue())
        print(i+1, q, c1, c2)

class Queue:
    def __init__(self, lst=None):
        self.items = lst
        if lst == None:
            self.items = []

    def __str__(self):
        return str(self.items)

    def enqueue(self, e):
        if e is not None:
            self.items.append(e)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0


if __name__ == "__main__":
    main()
