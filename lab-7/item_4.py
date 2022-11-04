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

    def preorder(self, curr=None):
        if curr == None:
            curr = self.root
        left = right = []
        if curr.left != None:
            left = self.preorder(curr.left)
        if curr.right != None:
            right = self.preorder(curr.right)
        if curr.left == None and curr.right == None:
            return [curr.data]
        return [curr.data] + left + right

    def inorder(self, curr=None):
        if curr == None:
            curr = self.root
        left = right = []
        if curr.left != None:
            left = self.inorder(curr.left)
        if curr.right != None:
            right = self.inorder(curr.right)
        if curr.left == None and curr.right == None:
            return [curr.data]
        return left + [curr.data] + right

    def postorder(self, curr=None):
        if curr == None:
            curr = self.root
        left = right = []
        if curr.left != None:
            left = self.postorder(curr.left)
        if curr.right != None:
            right = self.postorder(curr.right)
        if curr.left == None and curr.right == None:
            return [curr.data]
        return left + right + [curr.data]

    def breadthorder(self, root=None):
        if root == None:
            root = self.root
        queue, result = [root], []

        while len(queue) != 0:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                result.append(curr.data)
                if curr.left != None:
                    queue.append(curr.left)
                if curr.right != None:
                    queue.append(curr.right)
        return result

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

if __name__ == "__main__":
    T = BST()
    raw_inp = input('Enter Input : ').split('/')
    inp = [int(i) for i in raw_inp[0].split()]
    for i in inp:
        root = T.insert(i)
    print("Preorder : " + " ".join(list(map(str, T.preorder()))))
    print("Inorder : " + " ".join(list(map(str, T.inorder()))))
    print("Postorder : " + " ".join(list(map(str, T.postorder()))))
    print("Breadth : " + " ".join(list(map(str, T.breadthorder()))))
