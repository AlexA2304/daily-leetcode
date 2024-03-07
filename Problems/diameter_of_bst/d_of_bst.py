'''
Given the root of a binary tree, return the length of the diameter
of the tree.

The diameter of a binary tree is the length of the longest path 
between any two nodes in a tree. This path may or may not pass 
through the root.

The length of a path between two nodes is represented by the 
number of edges between them.
'''

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.diameter

    def helper(self, node: Optional[TreeNode]) -> int:
        if not node:
            return -1

        leftHeight = self.helper(node.left)
        rightHeight = self.helper(node.right)

        self.diameter = max(self.diameter, leftHeight + rightHeight + 2)

        return max(leftHeight, rightHeight) + 1
    
# Runtime: 46 ms -- beats 34.21% of users with Python3
# Memory: 19.22 mb -- beats 5.31% of users with Python3 
# (Can't seem to get these numbers any better on my machine)