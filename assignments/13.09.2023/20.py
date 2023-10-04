class Solution:
    def isValid(self, s: str) -> bool:
        st=[0]
        i=0
        for j in(s):
            st.append(j)
            if((st[i]==')' and st[i-1]=="(" ) or (st[i]=="}" and st[i-1]=="{") or (st[i]=="]" and st[i-1]=="[")):
                st.pop()
                st.pop()
            i+=1
        if(len(st)==1):
            return True
        else:
            return False

# or for refrence
 class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')', '{':'}','[':']'}

        for c in s:
            if c in brackets:
                stack.append(c)
            elif stack and c == brackets[stack.pop()]:
                continue
            else:
                return False
        
        return not stack
        
        
        