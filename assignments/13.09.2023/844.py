class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        cd=[]
        for i in s:
            if(i=='#' and len(stack)==0 ):
                  pass
            if(i=='#' and len(stack)!=0):
                stack.pop()
            if(i!='#'):
                stack.append(i)
        for j in t:
            if(j=='#' and len(cd)==0 ):
                pass
            if(j=='#'and len(cd)!=0):
                cd.pop()
            if(j!='#'):
                cd.append(j)
        if(cd==stack):
            return True
        else:
            return False
        
        