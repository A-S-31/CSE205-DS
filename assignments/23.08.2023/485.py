class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s=0
        k=0
        for i in range(len(nums)):
            if(nums[i]==1):
                s+=1
            else:
                if(k<=s):
                    k=s
                s=0
        if(s>=k):
            return s
        else:
            return k
