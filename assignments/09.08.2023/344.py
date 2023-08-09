class Solution:
    def reverseString(self, s: List[str]) -> None:

        def r(s,i,n): 
            if(i>=n):
                return s
            s[i],s[n]=s[n],s[i]
            r(s,i+1,n-1)
    
        r(s,0,len(s)-1)
            

