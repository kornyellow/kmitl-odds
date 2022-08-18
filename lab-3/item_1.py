class Stack:
    def __init__(self, l=None):
        if l == None:
            self.items = []
        else:
            self.items = l

    def push(self, e):
        self.items.append(e)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

print(" *** Stack implement by Python list***")
ls = [e for e in input("Enter data to stack : ").split()]
s = Stack()

for e in ls:
    s.push(e)

print(s.size(), "Data in stack : ", s.items)
while not s.isEmpty():
    s.pop()
print(s.size(), "Data in stack : ", s.items)
