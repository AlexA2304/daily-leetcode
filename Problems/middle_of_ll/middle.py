'''
Given the head of a singly linked list, return the middle node
of the linked list.

If there are two middle nodes, return the second middle node.
'''

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
# Runtime: 29 ms -- beats 89.83% of users with Python3
# Memory: 13.94 mb -- beats 100.00% of users with Python3 ;)