# Understanding the problem statement and the requirements.

# Task 5: Binary Search Tree (BST) – Insertion
# Implement a BST insertion algorithm.
# Allow the user to insert multiple integers and then print the in-order traversal of the tree.

# Let's start coding to create a Binary Search Tree (BST) and insert elements into it:
class TreeNode: # Represents a node in the BST
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree: # Represents the BST itself
    # Initialize the BST with no root
    def __init__(self): 
        self.root = None

    def insert(self, key): # Insert a new key into the BST
        # If the tree is empty, set the root to the new key
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key): # Helper function to insert a key recursively
        # Compare the key with the current node's value
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_rec(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_rec(node.right, key)

    def in_order_traversal(self, node): # Perform in-order traversal to print the BST in sorted order
        # Traverse the left subtree, visit the node, then traverse the right subtree
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.val, end=' ')
            self.in_order_traversal(node.right)

    def print_in_order(self):
        self.in_order_traversal(self.root)
        print()

# Custom function to simulate a list of values without using list literals or append
def get_numbers():
    nums = [0] * 7  # Create fixed-size array
    nums[0] = 7
    nums[1] = 3
    nums[2] = 9
    nums[3] = 1
    nums[4] = 5
    nums[5] = 8
    nums[6] = 10
    return nums

# Example usage:
bst = BinarySearchTree()
# Insert multiple integers into the BST
numbers = get_numbers()
for i in range(7):
    bst.insert(numbers[i])

# Print the in-order traversal of the BST
print("In-order Traversal of the BST:")
bst.print_in_order()

# This code defines a Binary Search Tree (BST) with insertion and in-order traversal methods.
# The user can insert multiple integers, and the in-order traversal will print them in sorted order.
# Example Input: 7, 3, 9, 1, 5, 8, 10
# Output: In-order Traversal of the BST: 1 3 5 7 8 9 10
# Created by Parkash Kumar
