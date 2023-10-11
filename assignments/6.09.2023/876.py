# Middle of the linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head=head
        self.next=next
        d=None
        n=0
        h=head
        while (head):
            head=head.next
            n+=1
        if(n%2==0):
            t=1
            while(t!=(n//2+1)):
                h=h.next
                t+=1
            return h
        if(n%2!=0):
            t=0
            while(t!=(n//2)):
                h=h.next
                t+=1
            return h


        