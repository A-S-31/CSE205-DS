# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(0)
        c=head
        carry=0

        while l1!=None or l2!=None or carry!=0:
            if l1:
                l1v=l1.val
            else:
                l1v=0
            l2v=l2.val if l2 else 0

            s=l1v+l2v+carry
            carry=s//10
            new=ListNode(s%10)
            c.next=new
            c=new
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return head.next
        