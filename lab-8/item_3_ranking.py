def main():
    raw_input = input("Enter Input : ")
    numbers, key = raw_input.split("/")
    key = int(key)
    numbers = list(map(int, numbers.split()))

    tree = BinarySearchTree()
    for num in numbers:
        tree.insert(num)
    tree.print(tree.root)
    print("-" * 50)

    rank = tree.get_rank_of(tree.root, key)
    print("Rank of %d : %d" % (key, rank))

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data, curr=None):
        if not self.root:
            self.root = Node(data)
            return
        if not curr:
            curr = self.root

        if data > curr.data:
            if curr.right:
                self.insert(data, curr.right)
            else:
                curr.right = Node(data)
        elif data <= curr.data:
            if curr.left:
                self.insert(data, curr.left)
            else:
                curr.left = Node(data)

    def get_rank_of(self, node, key):
        if not node:
            return 0

        rank_left = rank_right = 0
        if node.left:
            rank_left = tree.get_rank_of(node.left, key)
        if node.right:
            rank_right = tree.get_rank_of(node.right, key)

        if node.data <= key:
            return 1 + rank_left + rank_right
        return rank_left + rank_right

    def print(self, root, level=0):
        if root:
            self.print(root.right, level + 1)
            print("     " * level, root.data)
            self.print(root.left, level + 1)


if __name__ == "__main__":
    main()
