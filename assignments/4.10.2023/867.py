class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        s=[]
        m=[]
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                m.append(matrix[j][i])
            
            s.append(m)
            m=[]
        return s



        