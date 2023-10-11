# Valid paranthesis

class Solution:
    def isValid(self, s: str) -> bool:
        g=[]
        for i in range(len(s)):
            if(len(g)==0):
                g.append(s[i])
            elif(s[i]=='}' and g[-1]=='{'):
                g.pop()
            elif(s[i]==']' and g[-1]=='['):
                g.pop()
            elif(s[i]==')' and g[-1]=='('):
                g.pop()
            else:
                g.append(s[i])
        return len(g)==0
        