# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            current = head.next 
            prev = head 
            dummyNode = ListNode()

            while current != None:
                prev.next = dummyNode
                dummyNode = prev
                prev = current
                current = current.next
            prev.next = dummyNode

            prev2 = prev
            head = prev.next
            while head.next != None: 
                prev2 = head
                head = head.next
            prev2.next = None
            head = prev
            return head