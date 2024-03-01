'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)

        current = dummyHead
        pointer1 = list1
        pointer2 = list2

        while pointer1 and pointer2:
            if pointer1.val < pointer2.val:
                current.next = pointer1
                pointer1 = pointer1.next
            else:
                current.next = pointer2
                pointer2 = pointer2.next
            current = current.next
        while pointer1:
            current.next = pointer1
            pointer1 = pointer1.next
            current = current.next
        while pointer2:
            current.next = pointer2
            pointer2 = pointer2.next
            current = current.next

        return dummyHead.next
    
# Runtime: 45 ms -- Beats 17.86% of users with Python 3
# Memory: 16.58 mb -- Beats 72.26% of users with Python 3