#combinations sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]

        def func(c,array,s):
            if (s==target):
                result.append(array)

            if(s>target):
                return
            
            for i in range(len(c)):
                func(c[i:], array+[c[i]],s+c[i])
        func(candidates,[],0)
        return result
        