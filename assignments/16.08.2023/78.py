class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def func(l,i,nums,tmp):
            if(i==l):
                result.append(tmp)
                return
            
            func(l,i+1,nums,tmp)
            func(l,i+1,nums,tmp+[nums[i]])

        func(len(nums),0,nums,[])
        return result

