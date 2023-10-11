class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[]
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]<nums[j]):
                    ans.append(nums[j])
                    break
            if (len(ans)==0 or i==len(ans)):
                for k in range(i):
                    if(nums[i]<nums[k]):
                        ans.append(nums[k])
                        break
            
            if(len(ans)==0 or i==len(ans)):
                ans.append(-1)
        return ans
                
                    