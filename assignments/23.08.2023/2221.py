# Triangular sum of an array

class Solution(object):
    def triangularSum(self, nums):
        
        def t(arr):
            if(len(arr)==1):
                return arr[0]
            newnums=[]
            for i in range(0,len(arr)-1):
                s=(arr[i]+arr[i+1]) %10
                newnums.append(s)

            
            return t(newnums)
        return t(nums)
    
# now using for loop

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        n=len(nums)
        if n==1:
           return nums[0]
        else:
            x=nums
            def func(x):
                newNums=[]
                if len(x)>1:
                
                    for i in range(len(x)-1):
                        newNums.append((x[i]+x[i+1])%10)
                    
                    x=newNums
                
                    return func(x)

                else:
                    return x[0]
                
                
            return func(x)