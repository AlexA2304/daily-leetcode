'''
Given the root of a binary tree, invert the tree, and return its root.
'''

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left

            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
    
# Runtime: 36 ms -- Beats 53.40% of users with Python 3
# Memory: 16.44 mb -- Beats 91.22% of users with Python 3