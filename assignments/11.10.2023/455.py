# assign cookies
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        c=0

        for i in range(len(g)):

            for j in range(len(s)):
                if(g[i]<=s[j]):
                    c+=1
                    s.pop(j)
                    break
                    
        return c