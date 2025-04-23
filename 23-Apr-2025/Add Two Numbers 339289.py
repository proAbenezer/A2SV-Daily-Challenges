# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reming = 0 
        dummyNode = ListNode()
        tail = dummyNode

        while l1 and l2:
            newVal = l1.val + l2.val
            newVal += reming 
            reming = 0 
            if newVal >= 10:
                num1 = newVal % 10
                newVal = newVal // 10
                reming = newVal % 10
                newVal = num1
            tail.next = ListNode(newVal)
            tail = tail.next       
            l1 = l1.next 
            l2 = l2.next
   

        while l1:
            newVal = reming + l1.val 
            if newVal >= 10:
                num = newVal % 10
                newVal = newVal // 10 
                reming = newVal % 10
                newVal = num
            else:
                reming = 0  
            tail.next = ListNode(newVal)
            tail = tail.next
            l1 = l1.next
        while l2:
            newVal = reming + l2.val 
            if newVal >= 10:
                num = newVal % 10
                newVal = newVal // 10 
                reming = newVal % 10
                newVal = num
            else:
                reming = 0 
            tail.next = ListNode(newVal)
            tail = tail.next
            l2 = l2.next
        if reming > 0:
            tail.next = ListNode(reming)

        return dummyNode.next