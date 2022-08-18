class Queue:
    def __init__(self, l=None):
        if l != None:
            self.items = l
        else:
            self.items = []

    def enqueue(self, e):
        self.items.append(e)
        return len(self.items)

    def dequeue(self):
        if len(self.items) == 0:
            return -1, -1
        e = self.items.pop(0)
        return e, 0

    def __str__(self):
        if len(self.items) == 0:
            return "Empty"
        return " ".join(list(map(str, self.items)))

ip = input("Enter Input : ").split(",")

queue = Queue()
for l in ip:
    if l == "D":
        e, i = queue.dequeue()
        if e != -1:
            print(e, i)
        else:
            print(-1)
    else:
        e = int(l.split(" ")[1])
        print(queue.enqueue(e))
print(queue)
