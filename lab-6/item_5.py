def convert_raw_list_to_linked_list(raw_list):
    head = ListNode()
    curr = head
    while True:
        curr.data = raw_list.pop(0)
        if len(raw_list) == 0:
            break
        curr.next = ListNode()
        curr = curr.next

    return head

class ListNode:
    def __init__(self, data=0):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, param=None):
        if isinstance(param, ListNode):
            head = param
        elif isinstance(param, list):
            head = convert_raw_list_to_linked_list(param)
        else:
            head = None

        if head is not None:
            self.head = head
            self.size = 1

            curr = self.head
            while curr.next is not None:
                curr = curr.next
                self.size += 1
            self.tail = curr
        else:
            self.head = self.tail = None
            self.size = 0

    def __str__(self):
        if self.head is None:
            return "Empty"

        ret = []

        curr = self.head
        while curr is not None:
            ret.append(str(curr.data))
            curr = curr.next

        return " -> ".join(ret)

    def print(self):
        if self.head is None:
            return ""

        ret = []

        curr = self.head
        while curr is not None:
            ret.append(str(curr.data))
            curr = curr.next

        return " ".join(ret)

    def enqueue(self, e):
        if not isinstance(e, ListNode):
            added_node = ListNode(e)
        else:
            added_node = e

        self.size += 1
        if self.tail is None:
            self.head = self.tail = added_node
            return

        self.tail.next = added_node
        self.tail = added_node

    def append_sort(self, e):
        if not isinstance(e, ListNode):
            added_node = ListNode(e)
        else:
            added_node = e

        self.size += 1
        if self.tail is None:
            self.head = self.tail = added_node
            return

        if int(added_node.data) > int(self.head.data):
            added_node.next = self.head
            self.head = added_node
            return

        curr = self.head
        while curr.next is not None:
            if int(added_node.data) > int(curr.next.data):
                added_node.next = curr.next
                curr.next = added_node
                return
            curr = curr.next

        self.size -= 1
        self.enqueue(added_node)

    def dequeue(self):
        if self.head is None and self.tail is None:
            return None
        elif self.head != self.tail:
            curr = self.head
            self.head = self.head.next
            curr.next = None
        elif self.head == self.tail:
            curr = self.head
            self.head = self.tail = None
        self.size -= 1

        return curr

    def is_empty(self):
        return self.size == 0

def put_linked_list_in_digit_linked_list(digit_linked_list, linked_list, i=-1):
    if linked_list.is_empty():
        return

    dequeued_node = linked_list.dequeue()
    node_data = dequeued_node.data

    if abs(i) > len(dequeued_node.data) or dequeued_node.data[i] == "-":
        first_digit = 0
    else:
        first_digit = int(node_data[i])

    digit_linked_list[first_digit].append_sort(dequeued_node)

    put_linked_list_in_digit_linked_list(digit_linked_list, linked_list, i)

def print_digit_linked_list(digit_linked_list, i=0):
    if i == 10:
        return

    print("%d : %s" % (i, digit_linked_list[i].print()))
    print_digit_linked_list(digit_linked_list, i+1)

def is_digit_linked_list_1_to_9_empty(digit_linked_list, i=1):
    if not digit_linked_list[i].is_empty():
        return False
    if i == 9:
        return True
    return True and is_digit_linked_list_1_to_9_empty(digit_linked_list, i+1)

def allocate_digit_linked_list(digit_linked_list, i=9):
    digit_linked_list.append(SinglyLinkedList())
    if i == 0:
        return digit_linked_list

    return allocate_digit_linked_list(digit_linked_list, i-1)

def radix_sort_digit_sub_process(new_digit_linked_list, digit_linked_list, n, i=9):
    put_linked_list_in_digit_linked_list(new_digit_linked_list, digit_linked_list[i], n)
    if i == 0:
        return
    radix_sort_digit_sub_process(new_digit_linked_list, digit_linked_list, n, i-1)

def radix_sort_sub_process(digit_linked_list, i=-2, rnd=1):
    print("------------------------------------------------------------")
    print("Round : %d" % rnd)
    print_digit_linked_list(digit_linked_list)

    if is_digit_linked_list_1_to_9_empty(digit_linked_list):
        return digit_linked_list[0], rnd

    new_digit_linked_list = allocate_digit_linked_list([])
    radix_sort_digit_sub_process(new_digit_linked_list, digit_linked_list, i)
    digit_linked_list = new_digit_linked_list

    return radix_sort_sub_process(digit_linked_list, i-1, rnd+1)

def radix_sort_descending(linked_list):
    digit_linked_list = allocate_digit_linked_list([])
    put_linked_list_in_digit_linked_list(digit_linked_list, linked_list)
    return radix_sort_sub_process(digit_linked_list)

input_raw_list = input("Enter Input : ").split()
input_linked_list = SinglyLinkedList(input_raw_list)
before_radix_sort_str = str(input_linked_list)
sorted_linked_list, rnd = radix_sort_descending(input_linked_list)
after_radix_sort_str = str(sorted_linked_list)

print("------------------------------------------------------------")
print("%d Time(s)" % (rnd-1))
print("Before Radix Sort : %s" % before_radix_sort_str)
print("After  Radix Sort : %s" % after_radix_sort_str)
