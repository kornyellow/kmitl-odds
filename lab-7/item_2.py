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
            return
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

    def min(self, curr=None):
        if curr == None:
            curr = self.root
        if curr.left == None:
            if curr.right != None:
                if curr.right.data > curr.data:
                    return curr.data
                else:
                    return self.min(curr.right)
        if curr.left == None and curr.right == None:
            return curr.data
        return self.min(curr.left)

    def max(self, curr=None):
        if curr == None:
            curr = self.root
        if curr.right == None:
            if curr.left != None:
                if curr.left.data < curr.data:
                    return curr.data
                else:
                    return self.min(curr.left)
        if curr.left == None and curr.right == None:
            return curr.data
        return self.max(curr.right)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

if __name__ == "__main__":
    T = BST()
    inp = [int(i) for i in input('Enter Input : ').split()]
    for i in inp:
        root = T.insert(i)
    T.printTree(root)
    print("--------------------------------------------------")
    print("Min : %d" % T.min())
    print("Max : %d" % T.max())
