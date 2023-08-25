class Solution(object):
    def findKthPositive(self, arr, k):
       s=[]
       j=1
       i=0
       while(True):
           if(i==len(arr)):
               break
           if(arr[i]!=j):
               s.append(j)
           if(arr[i]==j):
               i+=1
           j+=1
       while(k+1>len(s)):
           s.append(j)
           j+=1
               
       return (s[k-1])
            
