class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        t=0
        
        for i in range(0,len(nums)):
            a=nums[i]
            s=str(a)
            if(len(s)%2==0):
                t+=1
        return t