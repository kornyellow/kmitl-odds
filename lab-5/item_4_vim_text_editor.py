def main():
    ip = input("Enter Input : ").split(",")

    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append("|")

    for e in ip:
        cursor_node = doubly_linked_list.findCursor()
        if e == "L":
            if cursor_node == doubly_linked_list.head:
                continue

            if cursor_node.prev.prev != None:
                cursor_node.prev.prev.next = cursor_node
            if cursor_node.next != None:
                cursor_node.next.prev = cursor_node.prev

            cursor_node.prev.next = cursor_node.next
            cursor_node.next = cursor_node.prev

            cursor_node.prev = cursor_node.prev.prev
            cursor_node.next.prev = cursor_node

            if cursor_node == doubly_linked_list.tail:
                doubly_linked_list.tail = cursor_node.next
            if cursor_node.next == doubly_linked_list.head:
                doubly_linked_list.head = cursor_node
        elif e == "R":
            if cursor_node == doubly_linked_list.tail:
                continue

            if cursor_node.next.next != None:
                cursor_node.next.next.prev = cursor_node
            if cursor_node.prev != None:
                cursor_node.prev.next = cursor_node.next

            cursor_node.next.prev = cursor_node.prev
            cursor_node.prev = cursor_node.next

            cursor_node.next = cursor_node.next.next
            cursor_node.prev.next = cursor_node

            if cursor_node == doubly_linked_list.head:
                doubly_linked_list.head = cursor_node.prev
            if cursor_node.prev == doubly_linked_list.tail:
                doubly_linked_list.tail = cursor_node
        elif e == "B":
            if cursor_node == doubly_linked_list.head:
                continue

            if cursor_node.prev == doubly_linked_list.head:
                doubly_linked_list.head = cursor_node
            cursor_node.prev = cursor_node.prev.prev
            if cursor_node.prev != None:
                cursor_node.prev.next = cursor_node
        elif e == "D":
            if cursor_node == doubly_linked_list.tail:
                continue

            if cursor_node.next == doubly_linked_list.tail:
                doubly_linked_list.tail = cursor_node
            cursor_node.next = cursor_node.next.next
            if cursor_node.next != None:
                cursor_node.next.prev = cursor_node
        else:
            doubly_linked_list.insert(doubly_linked_list.index("|"), e.split()[1])
    print(doubly_linked_list)

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
        return " ".join(ret)

    def reverse(self):
        if self.size == 0:
            return "Empty"

        ret = []
        head = self.tail
        while head != None:
            ret.append(str(head.value))
            head = head.prev
        return " ".join(ret)

    def index(self, query):
        node = self.head
        i = 0
        while node != None:
            if str(node.value) == str(query):
                return i
            node = node.next
            i += 1
        return -1

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

    def prepend(self, element):
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

    def findCursor(self):
        if self.head == None:
            return None

        node = self.head
        while node != None:
            if node.value == "|":
                return node
            node = node.next

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

    def insert(self, index, element):
        if type(element) != ListNode:
            node = ListNode(element)
        else:
            node = Element

        if index >= self.size:
            self.append(node)
            return
        elif self.size + index <= 0 or index == 0:
            self.prepend(node)
            return
        elif index < 0 and self.size + index > 0:
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


class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


if __name__ == "__main__":
    main()
