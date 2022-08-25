class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def __str__(self):
        return "Linked List : " + self.str()

    def str(self):
        if self.size == 0:
            return "Empty"

        ret = []
        tail = self.head
        while tail != None:
            ret.append(str(tail.value))
            tail = tail.next
        return " ".join(ret)

    def reverse(self):
        if self.size == 0:
            return "Linked List Reverse : Empty"

        ret = []
        head = self.tail
        while head != None:
            ret.append(str(head.value))
            head = head.prev
        return "Linked List Reverse : " + " ".join(ret)

    def append(self, element):
        if type(element) != ListNode:
            node = ListNode(element)
        else:
            node = element

        if self.head == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def addHead(self, element):
        if type(element) != ListNode:
            node = ListNode(element)
        else:
            node = element

        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def search(self, query):
        i = self.index(query)
        if i == -1:
            return "Not Found"
        return "Found"

    def index(self, query):
        node = self.head
        i = 0
        while node != None:
            if str(node.value) == str(query):
                return i
            node = node.next
            i += 1
        return -1

    def pop(self, index=-1):
        if index == -1:
            index = self.size - 1

        if index >= self.size or index < 0 or self.head == None:
            return "Out of Range"

        if index == 0:
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        else:
            node = self.head
            while index > 1:
                node = node.next
                index -= 1

            node.next = node.next.next
            if node.next != None:
                node.next.prev = node

        self.size -= 1
        return "Success"

    def insert(self, index, element):
        if type(element) != ListNode:
            node = ListNode(element)
        else:
            node = Element

        if index >= self.size:
            self.append(node)
            return
        elif self.size + index <= 0:
            self.addHead(node)
            return
        elif self.size + index > 0:
            index = self.size + index

        if self.head == None:
            self.head = self.tail = node
        else:
            insert = self.head
            while index > 1:
                insert = insert.next
                index -= 1
            node.next = insert.next
            node.next.prev = node
            node.prev = insert
            insert.next = node

        self.size += 1
        return 0

    def isEmpty(self):
        return self.size == 0

class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

ip = input("Enter Input : ").split(",")

doubly_linked_list = DoublyLinkedList()
for e in ip:
    if len(e.split()) == 1:
        command = e
        if command == "SI":
            print("Linked List size = " + str(doubly_linked_list.size) + " :", doubly_linked_list.str())
    elif len(e.split()) == 2:
        command, data = tuple(e.split())

        if command == "AP":
            doubly_linked_list.append(data)
        elif command == "AH":
            doubly_linked_list.addHead(data)
        elif command == "SE":
            print(doubly_linked_list.search(data), data, "in", doubly_linked_list.str())
        elif command == "ID":
            print("Index (" + data + ") =", doubly_linked_list.index(data), ":", doubly_linked_list.str())
        elif command == "PO":
            before_pop = doubly_linked_list.str()
            result = doubly_linked_list.pop(int(data))
            print(result, "|", before_pop, end=" ")
            if result == "Success":
                print("->", doubly_linked_list.str())
            else:
                print()
    else:
        command, index, data = tuple(e.split())

        if command == "IS":
            doubly_linked_list.insert(int(index), data)

print(doubly_linked_list)
print(doubly_linked_list.reverse())
