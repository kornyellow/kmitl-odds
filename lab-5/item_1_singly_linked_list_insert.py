def main():
    ip = input("Enter Input : ").split(",")
    raw_list = ip[0].split()

    linked_list = LinkedList()
    for e in raw_list:
        linked_list.append(e)
    print(linked_list)

class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def __str__(self):
        if self.is_empty():
            return "List is empty"

        ret = []
        curr = self.head
        while curr != None:
            ret.append(str(curr.data))
            curr = curr.next
        return "link list : " + ("->".join(ret))

    def append(self, data):
        if type(data) != ListNode:
            added_node = ListNode(data)
        else:
            added_node = data

        if self.head == None:
            self.head = self.tail = added_node
        else:
            self.tail.next = added_node
            self.tail = added_node
        self.size += 1

    def insert(self, index, element):
        if index > self.size or index < 0:
            return -1

        if type(element) != ListNode:
            node = ListNode(element)
        else:
            node = Element

        if self.head == None:
            self.head = self.tail = node
        else:
            if index == 0:
                node.next = self.head
                self.head = node
            else:
                insert = self.head
                while index > 1:
                    insert = insert.next
                    index -= 1
                node.next = insert.next
                insert.next = node

        self.size += 1
        return 0

    def is_empty(self):
        return self.size == 0


if __name__ == "__main__":
    main()
