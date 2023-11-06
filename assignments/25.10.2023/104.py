# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        l=[]
        def d(c,root,l):
            if root==None:
                l.append(c)
                c=0
                return 
            d(c+1,root.left,l)
            d(c+1,root.right,l)
        d(0,root,l)
        return max(l)
        





        