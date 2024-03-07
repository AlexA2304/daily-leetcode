'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along 
the longest path from the root node down to the farthest 
leaf node.
'''

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0
        def dfs(root):
            nonlocal depth

            if not root: 
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            depth = max(depth, 1 + left, 1 + right)

            return 1 + max(left, right)

        dfs(root)
        return depth
    
# Runtime: 36 ms -- beats 81.07% of users with Python3
# Memory: 17.64 mb -- beats 61.02% of users with Python3