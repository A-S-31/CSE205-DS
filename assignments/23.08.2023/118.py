class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        
        t=[[1]]

        for i in range(1,numRows):
            prev=t[-1]
            new=[1]

            for j in range(1,len(prev)):
                new.append(prev[j-1]+prev[j])
            
            new.append(1)
            t.append(new)
        return t