# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
       self.head=head
       self.next=next
       t=0
       a=1
       h=head
       while (h):
           h=h.next
           t+=1
       size=t-n
       if(t==1):
           return None
       y=head # previous element
       if(size==0):
           return head.next
       while(a<size):
           y=y.next
           a+=1
       y.next=y.next.next
       return head
           
           
      
