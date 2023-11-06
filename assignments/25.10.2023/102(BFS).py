# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# BFS algorithm(Breadth first level)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        R=[]
        q=collections.deque()

        q.append(root)

        while q:
            l=[]  # level
            for i in range(len(q)):
                n=q.popleft()
                if n:
                    l.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if l:
                R.append(l)
        return R


