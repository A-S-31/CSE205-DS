#Mergeing to 2 sorted list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d=f=ListNode()
        while list1!=None and list2!=None:
            if list1.val<list2.val:
                f.next=list1
                f=list1
                list1=list1.next
               
            else:
                f.next=list2
                f=list2
                list2=list2.next
                
        if(list1 or list2):         # which list is not empty   
               if(list1):
                   f.next=list1
               else:
                   f.next=list2
        

        return d.next