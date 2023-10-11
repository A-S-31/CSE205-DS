#INTERSECTION OF TWO LINKED LISTS


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
       f=[]
       c=headA

       while c:
           f.append(c)
           c=c.next
       c=headB

       while c:
           if c in f:
               return c
           c=c.next

       return None

