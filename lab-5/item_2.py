class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def __str__(self):
        if self.is_empty():
            return "Empty"

        ret = []
        curr = self.head
        while curr != None:
            ret.append(str(curr.data))
            curr = curr.next
        return " ".join(ret)

    def reverse(self):
        if self.is_empty():
            return "Empty"

        ret = []
        curr = self.tail
        while curr != None:
            ret.append(str(curr.data))
            curr = curr.prev
        return " ".join(ret)

    def append(self, data):
        if type(data) != ListNode:
            added_node = ListNode(data)
        else:
            added_node = data

        if self.head == None:
            self.head = self.tail = added_node
        else:
            self.tail.next = added_node
            added_node.prev = self.tail
            self.tail = added_node
        self.size += 1

    def prepend(self, data):
        if type(data) != ListNode:
            added_node = ListNode(data)
        else:
            added_node = data

        if self.head == None:
            self.head = self.tail = added_node
        else:
            added_node.next = self.head
            self.head.prev = added_node
            self.head = added_node
        self.size += 1

    def search(self, query):
        i = self.index(query)
        if i == -1:
            return "Not Found"
        return "Found"

    def index(self, query):
        curr = self.head
        i = 0
        while curr != None:
            if str(curr.data) == str(query):
                return i
            curr = curr.next
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
            curr = self.head
            while index > 1:
                curr = curr.next
                index -= 1

            curr.next = curr.next.next
            if curr.next != None:
                curr.next.prev = curr

        self.size -= 1
        return "Success"

    def insert(self, index, data):
        if type(data) != ListNode:
            added_node = ListNode(data)
        else:
            added_node = data

        if index >= self.size:
            self.append(added_node)
            return
        elif self.size + index <= 0:
            self.prepend(node)
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

    def is_empty(self):
        return self.size == 0

ip = input("Enter Input : ").split(",")

doubly_linked_list = DoublyLinkedList()
for e in ip:
    if len(e.split()) == 1:
        command = e
        if command == "SI":
            print("Linked List size = " + str(doubly_linked_list.size) + " :", str(doubly_linked_list))
    elif len(e.split()) == 2:
        command, data = tuple(e.split())

        if command == "AP":
            doubly_linked_list.append(data)
        elif command == "AH":
            doubly_linked_list.prepend(data)
        elif command == "SE":
            print(doubly_linked_list.search(data), data, "in", doubly_linked_list.str())
        elif command == "ID":
            print("Index (" + data + ") =", doubly_linked_list.index(data), ":", doubly_linked_list.str())
        elif command == "PO":
            before_pop = str(doubly_linked_list)
            result = doubly_linked_list.pop(int(data))
            print(result, "|", before_pop, end=" ")
            if result == "Success":
                print("->", str(doubly_linked_list))
            else:
                print()
    else:
        command, index, data = tuple(e.split())

        if command == "IS":
            doubly_linked_list.insert(int(index), data)

print("Linked List :", doubly_linked_list)
print("Linked List Reverse :", doubly_linked_list.reverse())
