# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        k = k % length
        if k == 0:
            return head

        steps_to_new_head = length - k
        current = head
        for _ in range(steps_to_new_head - 1):
            current = current.next

        new_head = current.next
        current.next = None
        tail.next = head

        return new_head
