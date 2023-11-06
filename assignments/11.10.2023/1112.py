#relative sorting array
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n=len(arr1)
        l=len(arr2)
        p=[]
        h=arr1.copy()
        for i in range(l):
            s=0
            for j in range(n):
                if(arr1[j]==arr2[i]):
                    p.append(arr1[j])
                    h.remove(arr1[j])
        h.sort()

        for t in h:
            p.append(t)
        return p





        