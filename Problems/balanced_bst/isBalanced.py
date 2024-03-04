'''
Given a binary tree, determine if it is 
height-balanced.
'''

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root) != -1

    def helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftHeight = self.helper(root.left)
        rightHeight = self.helper(root.right)

        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1
        
        return max(leftHeight, rightHeight) + 1
    
# Runtime: 40 ms -- beats 85.74% of users with Python3
# Memory: 17.58 mb -- beats 90.47% of users with Python3