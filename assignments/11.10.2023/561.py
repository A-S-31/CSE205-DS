# partition array
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=[]
        s=0
        for i in range(0,len(nums)-1,2):
            l.append(min(nums[i],nums[i+1]))
        print(l)
        for j in range(len(l)):
            s+=l[j]
        return s
