class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            j=i
            while(j>0 and nums[j-1]>nums[j]):
                nums[j],nums[j-1]=nums[j-1],nums[j]
                j-=1
                
        for k in range(0,len(nums)-1):
            if(nums[k+1]!=int(nums[k])+1):
                s=int(nums[k])+1
                return s      
            