class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if(len(nums)==0 or len(nums)==1 or len(nums)==2):
            return -1
        for i in range(1,len(nums)):
            j=i
            while j>0 and nums[j-1]>nums[j]:
                nums[j],nums[j-1]=nums[j-1],nums[j]
                j-=1
        return nums[1]
        
        