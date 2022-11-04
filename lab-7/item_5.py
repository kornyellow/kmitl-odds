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

    def checkpos(self, key, curr):
        if curr == None:
            return True
        if self.root.data == int(key):
            print("Root")
            return False
        if curr.left == None and curr.right == None:
            if curr.data == int(key):
                print("Leaf")
                return False
        if curr.data == int(key):
            print("Inner")
            return False
        return self.checkpos(key, curr.left) and self.checkpos(key, curr.right)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

if __name__ == "__main__":
    T = BST()
    inp = [int(i) for i in input('Enter Input : ').split()]
    for i in range(1, len(inp)):
        root = T.insert(inp[i])
    T.printTree(root)
    if T.checkpos(inp[0], root):
        print("Not exist")
