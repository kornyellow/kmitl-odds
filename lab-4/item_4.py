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


def main():
    ip = input("Enter Input : ").split("/")
    data = ip[0].split(",")
    cms = ip[1].split(",")

    tp = {}
    for d in data:
        k, e = d.split(" ")
        if k not in tp:
            tp[k] = []
        tp[k].append(e)

    a = {}
    for cm in cms:
        if cm == "D":
            is_found = False
            b = a.copy()
            for k in b:
                if a[k].size() == 0:
                    continue
                else:
                    e = a[k].dequeue()
                    is_found = True
                    print(e)
                    break
            for k in b:
                if a[k].size() == 0:
                    del a[k]
            if not is_found:
                print("Empty")
        else:
            e = cm.split(" ")[1]
            for b in tp:
                if e in tp[b]:
                    if b not in a:
                        a[b] = Queue()
                    a[b].enqueue(e)

if __name__ == "__main__":
    main()
