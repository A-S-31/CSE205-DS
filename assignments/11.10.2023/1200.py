class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans=[]
        
        tmp=float('inf')# it indicates the value infinity
# calculated the minimum difference

        for k in range(0,len(arr)-1):
            s=arr[k+1]-arr[k]
            if(s<tmp):
                tmp=s
# finding pairs with minimum difference            
        for u in range(0,len(arr)-1):
            s=arr[u+1]-arr[u]
            if s==tmp:
                ans.append([arr[u],arr[u+1]])
        return ans    



        