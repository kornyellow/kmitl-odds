def main():
    inp = list(map(int, input("Enter Input : ").split()))

    tree = BST()
    tree.root = to_tree(inp)
    tree.print(tree.root)

    print(tree.is_valid())

def to_tree(l, i=0):
    if i >= len(l) or l[i] == None:
        return None
    d = l[i]
    lf = (i * 2) + 1
    rt = lf + 1
    t = Node(d)
    t.left = to_tree(l, lf)
    t.right = to_tree(l, rt)
    return t

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def print(self, curr, level=0):
        if curr:
            self.print(curr.right, level + 1)
            print('     ' * level, curr.data)
            self.print(curr.left, level + 1)

    def is_valid(self):
        def check(root, l=0, h=100):
            if root is None:
                return True
            if root.data < l or root.data > h:
                return False
            return (check(root.left, l, root.data - 1)) and (check(root.right, root.data + 1, h))
        return check(self.root)


if __name__ == "__main__":
    main()
