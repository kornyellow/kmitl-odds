class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


def create_linked_list(lst):
    dummy = curr = ListNode()
    for e in lst:
        curr.next = ListNode(e)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    curr = head
    ret = []
    while curr:
        ret.append(str(curr))
        curr = curr.next
    return " ".join(ret)

def merge_linked_list(ll1, ll2):
    dummy = curr = ListNode()
    while ll1 and ll2:
        if int(str(ll1)) < int(str(ll2)):
            curr.next = ll1
            ll1 = ll1.next
        else:
            curr.next = ll2
            ll2 = ll2.next
        curr = curr.next
    if ll1 or ll2:
        curr.next = ll1 if ll1 else ll2
    return dummy.next

def main():
    l1, l2 = input("Enter 2 Lists : ").split()

    ll1 = create_linked_list(l1.split(","))
    ll2 = create_linked_list(l2.split(","))
    print("LL1 :", print_linked_list(ll1))
    print("LL2 :", print_linked_list(ll2))

    ll3 = merge_linked_list(ll1, ll2)
    print("Merge Result :", print_linked_list(ll3))

if __name__ == "__main__":
    main()
