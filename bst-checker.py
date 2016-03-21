"""
Write a function to check that a binary tree is a valid binary search tree
A binary search tree is a binary tree in which, for each node:

    The node's value is greater than all values in the left subtree.
    The node's value is less than all values in the right subtree.

BSTs are useful for quick lookups. If the tree is balanced, we can search for a
given value in the tree in O(\lg{n})O(lgn) time.
Here's a sample binary tree node class:

    class BinaryTreeNode:
	def __init__(self, value):
	    self.value = value
	    self.left  = None
	    self.right = None

	def insert_left(self, value):
	    self.left = BinaryTreeNode(value)
	    return self.left

	def insert_right(self, value):
	    self.right = BinaryTreeNode(value)
	    return self.right
"""

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def is_valid_search_tree(self):
        right_is_balanced = left_is_balanced = False
        if self.right is None:
            right_is_balanced = True
        elif self.right.value > self.value:
            right_is_balanced = self.right.is_valid_search_tree()

        if self.left is None:
            left_is_balanced = True
        elif self.left.value < self.value:
            left_is_balanced = self.left.is_valid_search_tree()

        return right_is_balanced and left_is_balanced


if __name__ == '__main__':
    tree = BinaryTreeNode(16)
    
    rsubtree = tree.insert_right(24)
    rsubtree.insert_left(20)
    rsubtree.insert_right(28)

    lsubtree = tree.insert_left(8)
    lsubtree.insert_left(4)
    lsubtree.insert_right(12)

    assert tree.is_valid_search_tree()
