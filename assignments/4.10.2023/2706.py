class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
           def func(l,i,prices,tmp):
               if i==l:
                   if(len(tmp)==2 and sum(tmp)<=3):
                       result.append(sum(tmp))
               func(l,i+1,prices,tmp)
               func(l,i+1,prices,tmp+[prices[i]])
           func(len(prices),0,prices,[])
           return money-max(result)

#above code has very high time complexity
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
           for i in range(len(prices)-1):
               for j in range(i,len(prices)-1):
                   if(prices[j]>prices[j+1]):
                       prices[j]=prices[j]+prices[j+1]
                       prices[j+1]=prices[j]-prices[j+1]
                       prices[j]=prices[j]-prices[j+1]
           if(prices[0]+prices[1]<=money):
               s=prices[0]+prices[1]
               return money-s
           else:
               return money


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
           for i in range(1,len(prices)):
               j=i
               while j>0  and prices[j-1]>prices[j]:
                   prices[j],prices[j-1]=prices[j-1],prices[j]
                   j-=1
            

           if(prices[0]+prices[1]<=money):
               s=prices[0]+prices[1]
               return money-s
           else:
               return money

            
            
            