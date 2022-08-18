class Queue:
    def __init__(self, l=None):
        if l != None:
            self.items = l
        else:
            self.items = []

    def enqueue(self, e):
        self.items.append(e)

    def dequeue(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

p, t = input("Enter people and time : ").split(" ")
p = [*p]
t = int(t)

queue = Queue(p)
c1 = Queue()
c2 = Queue()
i = 0
j = -1
for _ in range(t):
    if i % 3 == 0:
        if c1.size() != 0:
            c1.dequeue()
    if j % 2 == 0:
        if c2.size() != 0:
            c2.dequeue()
    if queue.size() != 0:
        if c1.size() < 5:
            c1.enqueue(queue.dequeue())
        else:
            if j == -1:
                j = 0
            c2.enqueue(queue.dequeue())
    print(i+1, queue.items, c1.items, c2.items)
    i += 1
    if j >= 0:
        j += 1
