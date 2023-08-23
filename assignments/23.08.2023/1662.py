class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        x=""
        y=""

        for i in range(0,len(word1)):
            x+=word1[i]
        for j in range(0,len(word2)):
            y+=word2[j]
        
        return(x==y)