# permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        
        def func(nums,tmp):
            if len(tmp)==len(nums):
                result.append(tmp)
                return        
            for j in range(len(nums)):
                if nums[j]  not in tmp:
                    func(nums,tmp+[nums[j]])
        func(nums,[])
        return result