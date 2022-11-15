def main():
    inp = input("Enter Input : ").split(",")

    queue = Queue()
    for e in inp:
        if e == "D":
            e = queue.dequeue()
            if e != -1:
                print(e, 0)
            else:
                print(-1)
        else:
            a = e.split()[1]
            queue.enqueue(a)
            print(queue.size())
    print(queue)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, e):
        self.items.append(e)

    def dequeue(self):
        if self.is_empty():
            return -1
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def __str__(self):
        if len(self.items) == 0:
            return "Empty"
        return " ".join(list(map(str, self.items)))


if __name__ == "__main__":
    main()
