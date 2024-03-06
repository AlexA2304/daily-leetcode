'''
Given the head of a singly linked list, reverse the list, 
and return the reversed list.
'''

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        current = head
        while current.next:
            holder = current.next
            current.next = holder.next
            holder.next = head
            head = holder
        return head
    
# Runtime: 32 ms -- beats 87.73% of users with Python3 :)
# Memory: 17.81 mb -- beats 30.74% of users with Python3