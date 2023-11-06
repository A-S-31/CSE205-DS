# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        c=root
        stack=[]
        r=[]
        while c or stack:
            if c:
                r.append(c.val)
                stack.append(c.right)
                c=c.left
            else:
                c=stack.pop()
        return r


        