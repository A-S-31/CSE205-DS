# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Post order traversal
class Solution:
    def p(self,n,l):
        if n is None:
            return
        self.p(n.left,l)
        self.p(n.right,l)
        l.append(n.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        self.p(root,l)
        return l

        