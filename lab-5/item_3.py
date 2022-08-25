class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def __str__(self):
        if self.size == 0:
            return "Empty"

        ret = []
        tail = self.head
        while tail != None:
            ret.append(str(tail.value))
            tail = tail.next
        return "".join(ret)

    def reverse(self):
        if self.size == 0:
            return "Empty"

        ret = []
        head = self.tail
        while head != None:
            ret.append(str(head.value))
            head = head.prev
        return "".join(ret)

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

    def clear(self):
        self.head = self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

def process_candies(doubly_linked_list):
    combo = 0
    while True:
        prev = doubly_linked_list.reverse()
        node = doubly_linked_list.head

        last_piece = None
        while node != None:
            if node.value != last_piece:
                match_count = 1
                last_piece = node.value
            else:
                match_count += 1

            if match_count == 3:
                if node.next != None:
                    node.next.prev = node.prev.prev.prev
                else:
                    doubly_linked_list.tail = node.prev.prev.prev
                if node.prev.prev.prev != None:
                    node.prev.prev.prev.next = node.next
                else:
                    doubly_linked_list.head = node.next

                doubly_linked_list.size -= 3
                combo += 1
                break
            node = node.next
        if prev == doubly_linked_list.reverse():
            break
    return combo

ip = input("Enter Input : ").split()

doubly_linked_list = DoublyLinkedList()
for e in ip:
    doubly_linked_list.append(e)
combo = process_candies(doubly_linked_list)
print(doubly_linked_list.size)
print(doubly_linked_list.reverse())
if combo >= 2:
    print("Combo :", combo, "! ! !")
