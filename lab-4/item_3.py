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

ip = input("Enter Input : ").split("/")
l = ip[0]
cms = ip[1].split(",")

book = Queue(l.split(" "))
for cm in cms:
    if cm == "D":
        book.dequeue()
    else:
        e = cm.split(" ")[1]
        book.enqueue(e)

seen = {}
check = book.items
is_dup = False
for c in check:
    if c in seen:
        is_dup = True
        break
    else:
        seen[c] = 1
if not is_dup:
    print("NO Duplicate")
else:
    print("Duplicate")
