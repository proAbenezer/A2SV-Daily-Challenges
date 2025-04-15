# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        

        leftNode = head 
        rightNode = head.next
        while rightNode:
            if rightNode.val == val:
                leftNode.next = rightNode.next
                rightNode.next = None
                rightNode = leftNode.next
            else:
                rightNode = rightNode.next
                leftNode = leftNode.next
        return head 
       

        