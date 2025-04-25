# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        cur = head 
        while cur:
            length += 1
            cur = cur.next
        baseLength = length // k
        remainder = length % k 
        
        cur = head 
        res = []
        for i in range(k):
            res.append(cur)
            for j in range(baseLength - 1 + (1 if remainder else 0)):
                if not cur: break 
                cur = cur.next
            remainder -= (1 if remainder else 0)
            if cur:
                cur.next, cur = None, cur.next
        return res