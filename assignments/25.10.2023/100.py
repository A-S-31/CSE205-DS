# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l=[]
        r=[]
        c=p
        d=q
        stack=[]

        while c or stack:
            if c:
                l.append(c.val)
                stack.append(c.right)
                c=c.left
            else:
                l.append(c)
                c=stack.pop()
        while d or stack:
            if d:
                r.append(d.val)
                stack.append(d.right)
                d=d.left
            else:
                r.append(d)
                d=stack.pop()
        print(l)
        print(r)
        return l==r
    
