class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        d=""
        for i in s:
            if(i=='*' and len(stack)==0):
                pass
            if(i=='*' and len(stack)!=0):
                stack.pop()
            if(i!='*'):
                stack.append(i)
        if(len(stack)==0):
            return ""
        for i in range(len(stack)):
            d+=stack[i]
        return d


        
        