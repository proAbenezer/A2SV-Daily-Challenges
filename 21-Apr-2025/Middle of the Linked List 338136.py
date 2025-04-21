# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        mid = (length // 2) + 1
        idx = 0 
        current = head
        while idx < mid - 1:
            current = current.next  
            idx += 1
        return current