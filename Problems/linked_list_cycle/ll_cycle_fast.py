

# Definition for singly-linked list.

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return False

        fast = slow = head

        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
    
# Runtime: 44 ms -- beats 67.05% of users with Python3
# Memory: 19.16 mb -- beats 50.88% of users with Python3