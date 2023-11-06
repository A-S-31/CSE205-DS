# sorting colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums)>1:
            left=nums[:len(nums)//2]
            right=nums[len(nums)//2:]

            self.sortColors(left)
            self.sortColors(right)
            i=0
            j=0
            k=0


            while i<len(left) and j<len(right):
                if right[j]<left[i]:
                    nums[k]=right[j]
                    j+=1
                else:
                    nums[k]=left[i]
                    i+=1
                k+=1
            while i<len(left):
                nums[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                nums[k]=right[j]
                j+=1
                k+=1
        return (nums)