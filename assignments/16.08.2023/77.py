#combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
       nums=[]
       for i in range(n):
           nums.append(i+1)
       res=[]
       s=[]
       def func(l,i,nums,tmp):
           if i==l:
               s.append(tmp)
               if(len(tmp)==k):
                   res.append(tmp)
               return
           func(l,i+1,nums,tmp)
           func(l,i+1,nums,tmp+[nums[i]])
       func(n,0,nums,[])
       return res

       
