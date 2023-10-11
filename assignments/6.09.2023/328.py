# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head=head
        self.next=next
        if self.head==None:
            return "List is empty"
        if self.head.next==None:
            return head
        h=self.head.next
        g=self.head
        e=h
        t=g

    
        while e!=None:
        
            t.next=t.next.next
            e.next=e.next.next
            t=t.next
            e=e.next
        t=h

        return g


                



        