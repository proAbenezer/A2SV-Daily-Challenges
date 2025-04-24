# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodeVal = []
        current = head
        while current:
            nodeVal.append(current.val)
            current = current.next
        left, right = 0, len(nodeVal) - 1
        res = 0 
        print(len(nodeVal))
        while left < right:
            res = max(res, nodeVal[left] + nodeVal[right])
            print(left, right, "  ", nodeVal[left], nodeVal[right])
            left += 1
            right -= 1
        return res