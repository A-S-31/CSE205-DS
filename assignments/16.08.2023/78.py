class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def s(a,w,res):
            
            if len(a)==0:
                res.append(w)
                return
            
            out1 = w[:]
            out2 = w[:]
            out2.append(a[0])
            s(a[1:],out1,res)
            s(a[1:],out2,res)
            return
        
        res = []
        w = []
        s(nums,w,res)
        return res