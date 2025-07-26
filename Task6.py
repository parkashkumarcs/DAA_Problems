# Let's first overview the
# problem statement and understand precisely what we need to do.   
# Task 6: Binary Search Tree (BST) – Deletion
# Extend the BST code to handle deletion of a node.
# Make sure to handle all three cases:
# - Node with no children
# - Node with one child
# - Node with two children

# Let's start coding to extend the Binary Search Tree (BST) with a deletion method:
class TreeNode:  # Represents a node in the BST
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
class BinarySearchTree:  # Represents the BST itself
    # Initialize the BST with no root
    def __init__(self):
        self.root = None
    def insert(self, key):  # Insert a new key into the BST
        # If the tree is empty, set the root to the new key
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_rec(self.root, key)
    def _insert_rec(self, node, key):  # Helper function to insert a key recursively
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
    def in_order_traversal(self, node):  # Perform in-order traversal to print the BST in sorted order
        # Traverse the left subtree, visit the node, then traverse the right subtree
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.val, end=' ')
            self.in_order_traversal(node.right)
    def print_in_order(self):
        self.in_order_traversal(self.root)
        print()
    def delete(self, key):  # Delete a node with the given key
        self.root = self._delete_rec(self.root, key)
    def _delete_rec(self, node, key):  # Helper function to delete a node recursively
        if node is None:
            return node
        # Traverse the tree to find the node to delete
        if key < node.val:
            node.left = self._delete_rec(node.left, key)
        elif key > node.val:
            node.right = self._delete_rec(node.right, key)
        else:
            # Node with one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete_rec(node.right, temp.val)
        return node
    def _min_value_node(self, node):  # Find the node with the minimum value
        current = node
        while current.left is not None:
            current = current.left
        return current
# Example usage:
bst = BinarySearchTree()
# Insert multiple integers into the BST
numbers = [7, 3, 9, 1, 5, 8, 10]
for number in numbers:
    bst.insert(number)
# Print the in-order traversal of the BST
print("In-order Traversal of the BST before deletion:")
bst.print_in_order()
# Delete a node from the BST
bst.delete(3)
# Print the in-order traversal of the BST after deletion
print("In-order Traversal of the BST after deleting 3:")
bst.print_in_order()
# This code extends the Binary Search Tree (BST) with a deletion method.
# The user can insert multiple integers, delete a specified integer, and the in-order traversal will print the remaining elements in sorted order.
# Example Input: 7, 3, 9, 1, 5, 8, 10 (inserted), delete 3
# Output: In-order Traversal of the BST before deletion: 1 3 5 7 8 9 10
# In-order Traversal of the BST after deleting 3: 1 5 7 8 9 10
# Created by Parkash Kumar:)))))))))))))))))))))))))
