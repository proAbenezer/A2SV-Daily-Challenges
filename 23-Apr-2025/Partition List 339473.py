# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        leftHead = ListNode()
        rightHead = ListNode()

        left = leftHead 
        right = rightHead

        cur = head 
        while cur:
            if cur.val < x:
               left.next = ListNode(cur.val)
               left = left.next
            else:
               right.next = ListNode(cur.val)
               right = right.next

            cur = cur.next
        left.next = ListNode(x)
        left.next = rightHead.next

        return leftHead.next 