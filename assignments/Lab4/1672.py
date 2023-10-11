class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        R=0
        s=0
        for i in range(len(accounts)):
            s=sum(accounts[i])
            if(s>R):
                R=s
        return R


        