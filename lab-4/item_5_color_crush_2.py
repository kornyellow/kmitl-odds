def main():
    normal, mirror = tuple(input("Enter Input (Normal, Mirror) : ").split())

    normal_queue = Queue([*normal])
    mirror_queue = Queue([*mirror])

    mirror_item, mirror_exp = process_candy(mirror_queue)
    failed = use_item(normal_queue, mirror_item)
    _, normal_exp = process_candy(normal_queue)

    print("NORMAL :")
    print(normal_queue.size())
    print(normal_queue)
    print(normal_exp-failed, "Explosive(s) ! ! ! (NORMAL)")

    if failed > 0:
        print("Failed Interrupted %d Bomb(s)" % (failed))

    print("------------MIRROR------------")
    print(": RORRIM")
    print(mirror_queue.size())
    print(mirror_queue.reverse())
    print("(RORRIM) ! ! ! (s)evisolpxE", mirror_exp)

def process_candy(candy_queue):
    item = Stack()
    explosion = 0

    queue_1 = Queue()
    queue_2 = Queue()

    old_candy = candy_queue.items.copy()
    while True:
        if candy_queue.is_empty() and queue_1.is_empty() and queue_2.is_empty():
            break
        elif candy_queue.is_empty() and queue_1.is_empty():
            while not queue_2.is_empty():
                candy_queue.enqueue(queue_2.dequeue())
            if candy_queue.items == old_candy:
                break
            old_candy = candy_queue.items.copy()
        else:
            if not queue_1.is_empty() and queue_1.first() != candy_queue.first():
                while not queue_1.is_empty():
                    queue_2.enqueue(queue_1.dequeue())
            else:
                c = candy_queue.dequeue()
                queue_1.enqueue(c)
                if queue_1.size() == 3:
                    queue_1.clear()
                    item.push(c)
                    explosion += 1

    return item, explosion

def use_item(candy_queue, item_stack):
    failed = 0

    queue_1 = Queue()
    queue_2 = Queue()
    while not item_stack.is_empty():
        if queue_1.size() == 2 and queue_1.first() == candy_queue.first():
            item = item_stack.pop()
            queue_1.enqueue(item)
            if item == queue_1.first():
                failed += 1
            queue_1.enqueue(candy_queue.dequeue())
            while not queue_1.is_empty():
                queue_2.enqueue(queue_1.dequeue())
        if queue_1.first() != candy_queue.first():
            while not queue_1.is_empty():
                queue_2.enqueue(queue_1.dequeue())
        if candy_queue.is_empty():
            break
        queue_1.enqueue(candy_queue.dequeue())

    while not queue_1.is_empty():
        queue_2.enqueue(queue_1.dequeue())
    while not candy_queue.is_empty():
        queue_2.enqueue(candy_queue.dequeue())
    while not queue_2.is_empty():
        candy_queue.enqueue(queue_2.dequeue())

    return failed

class Queue:
    def __init__(self, lst=None):
        self.items = lst
        if lst == None:
            self.items = []

    def __str__(self):
        if self.is_empty():
            return "Empty"
        x = self.items.copy()
        x.reverse()
        return "".join(x)

    def reverse(self):
        if self.is_empty():
            return "ytpmE"
        return "".join(self.items)

    def enqueue(self, e):
        self.items.append(e)

    def dequeue(self):
        return self.items.pop(0)

    def first(self):
        if not self.is_empty():
            return self.items[0]

    def clear(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0


class Stack:
    def __init__(self):
        self.items = []

    def push(self, e):
        self.items.append(e)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0


if __name__ == "__main__":
    main()
