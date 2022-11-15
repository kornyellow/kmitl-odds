def main():
    binary_tree = BST()
    raw_inp = input('Enter Input : ').split('/')
    inp = [int(i) for i in raw_inp[0].split()]
    for i in inp:
        root = binary_tree.insert(i)
    binary_tree.print_tree(root)
    print("--------------------------------------------------")
    print(binary_tree.min_count(raw_inp[1]))

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if self.root == None:
            self.root = Node(data)
            return self.root
        curr = self.root
        while True:
            if node.data > curr.data:
                if curr.right != None:
                    curr = curr.right
                else:
                    curr.right = node
                    break
            else:
                if curr.left != None:
                    curr = curr.left
                else:
                    curr.left = node
                    break
        return self.root

    def min_count(self, key, node=None):
        if node == None:
            node = self.root
        s = 0
        if node.data <= int(key):
            s = 1
        if node.right != None:
            s += self.min_count(key, node.right)
        if node.left != None:
            s += self.min_count(key, node.left)
        return s

    def print_tree(self, node, level = 0):
        if node != None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)

if __name__ == "__main__":
    main()
