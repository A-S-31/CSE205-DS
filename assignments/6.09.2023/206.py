"""Algorithm for reversed linked list"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head=head
        self.next=next
        d=None
       # t=head
        while (head!=None):
          t=head.next
          head.next=d
          d=head
          head=t
        return d
