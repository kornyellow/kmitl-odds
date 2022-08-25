class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def createLinkedList(raw_list):
    head = ListNode()
    node = head
    while True:
        node.value = raw_list.pop(0)
        if len(raw_list) == 0:
            break
        node.next = ListNode()
        node = node.next
    return head

def printLinkedList(head):
    ret = []
    tail = head
    while tail != None:
        ret.append(str(tail.value))
        tail = tail.next
    return " ".join(ret)

def size(head):
    size = 0
    node = head
    while node != None:
        node = node.next
        size += 1
    return size

def bottomup(head, b, size):
    cut_index = int(size * (b/100))
    first = head
    node = head
    if cut_index > 1:
        while True:
            node = node.next
            cut_index -= 1
            if cut_index == 1:
                head = node.next
                node.next = None
                break
    else:
        head = node.next
        node.next = None

    node = head
    if node.next != None:
        while True:
            node = node.next
            if node.next == None:
                break
    node.next = first

    return head

def riffle(head, r, size):
    if int(r/10) == 0 or int(r/10) == 10:
        return head

    cut_index = int(size * (r/100))

    first_head = head
    second_head = None

    node = head
    if cut_index > 0:
        while True:
            cut_index -= 1
            if cut_index == 0:
                second_head = node.next
                node.next = None
                break
            node = node.next
    else:
        second_head = node.next
        node.next = None

    first_node = first_head
    second_node = second_head

    head = ListNode()
    result = head
    while True:
        result.value = first_node.value
        if first_node.next != None:
            result.next = ListNode()
        else:
            result.next = second_node
            break

        if first_node.next != None:
            first_node = first_node.next
        result = result.next

        result.value = second_node.value
        if second_node.next != None:
            result.next = ListNode()
        else:
            result.next = first_node
            break

        if second_node.next != None:
            second_node = second_node.next
        result = result.next

    return head

def deriffle(head, r, size):
    cut_index = min(size - int(size * (r/100)), int(size * r/100))
    if cut_index == 0:
        return head

    first_head = ListNode()
    second_head = ListNode()
    first_node = first_head
    second_node = second_head

    node = head
    while True:
        first_node.value = node.value
        if cut_index > 1:
            first_node.next = ListNode()
            first_node = first_node.next
        node = node.next

        second_node.value = node.value
        if cut_index > 1:
            second_node.next = ListNode()
            second_node = second_node.next
        node = node.next

        cut_index -= 1
        if node == None:
            break
        elif cut_index == 0:
            if r >= 50:
                first_node.next = node
            else:
                second_node.next = node
            break

    tail = first_head
    while True:
        if tail.next == None:
            break
        tail = tail.next
    tail.next = second_head

    return first_head

def debottomup(head, b, size):
    cut_index = size - int(size * (b/100))
    first = head
    node = head

    if cut_index > 1:
        while True:
            node = node.next
            cut_index -= 1
            if cut_index == 1:
                head = node.next
                node.next = None
                break
    else:
        head = node.next
        node.next = None

    node = head
    if node.next != None:
        while True:
            node = node.next
            if node.next == None:
                break
    node.next = first

    return head

def scramble(head, b, r, size):
    print("Start :", printLinkedList(head))
    head = bottomup(head, b, size)
    print("BottomUp %.3f %% :" % (b), printLinkedList(head))
    head = riffle(head, r, size)
    print("Riffle %.3f %% :" % (r), printLinkedList(head))
    head = deriffle(head, r, size)
    print("Deriffle %.3f %% :" % (r), printLinkedList(head))
    head = debottomup(head, b, size)
    print("Debottomup %.3f %% :" % (b), printLinkedList(head))
    return head

raw_list, commands = tuple(input("Enter Input : ").split("/"))

head = createLinkedList(raw_list.split())
print("--------------------------------------------------")
for e in commands.split("|"):
    x, y = tuple(e.split(","))
    if x[0] == "B":
        b, r = float(x.split()[1]), float(y.split()[1])
    else:
        r, b = float(x.split()[1]), float(y.split()[1])
    head = scramble(head, b, r, size(head))
    print("--------------------------------------------------")
