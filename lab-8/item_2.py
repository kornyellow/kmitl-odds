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

    def closest_value(self, root, key, min_diff=2E31, min_diff_key=-1):
        if not root:
            return min_diff_key

        # Check if key itself is present
        if root.data == key:
            min_diff_key = key

        # Update min_diff and min_diff_key by checking current node's data
        if min_diff > abs(root.data - key):
            min_diff = abs(root.data -key)
            min_diff_key = root.data

        # If key is less than current node's data meaning we don't have
        # to check right side
        if key < root.data:
            return self.closest_value(root.left, key, min_diff, min_diff_key)
        return self.closest_value(root.right, key, min_diff, min_diff_key)

    def print(self, root, level=0):
        if root:
            self.print(root.right, level + 1)
            print("     " * level, root.data)
            self.print(root.left, level + 1)

if __name__ == "__main__":
    # Get user input
    raw_input = input("Enter Input : ")
    numbers, key = raw_input.split("/")
    key = int(key)
    numbers = list(map(int, numbers.split()))

    # Create tree insert numbers and print
    tree = BinarySearchTree()
    for num in numbers:
        tree.insert(num)
        tree.print(tree.root)
        print("-" * 50)

    # Find closest value
    closest_values = tree.closest_value(tree.root, key)
    print("Closest value of %d : %d" % (key, closest_values))
