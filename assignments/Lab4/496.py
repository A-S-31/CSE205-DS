class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in range (len(nums1)):
            for j in range (len(nums2)):
                if(nums1[i]==nums2[j]):
                    for k in range(j+1,len(nums2)):
                        if(nums2[j]<nums2[k]):
                            ans.append(nums2[k])
                            break
                    if(len(ans)==0 or i==len(ans)): 
                        ans.append(-1)
        
        return ans                    


        