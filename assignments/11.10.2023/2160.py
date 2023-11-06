#minimum sum of four digits

class Solution:
    def minimumSum(self, num: int) -> int:
        l=[]
        # extracting all the digits from the number and storing it inside the list
        for i in str(num):
            l.append(int(i))
        
 # using bubble sort for sorting the array
        for j in range(len(l)):
            s=0

            for k in range(0,len(l)-j-1):
                if(l[k]>l[k+1]):
                    l[k],l[k+1]=l[k+1],l[k]
                    s=1
            if(s==0):
                break
        # finding the smallest digit and putting it on tens position in both the numbers and larger digits
        # to the ones position in both numbers using concatenation 
        # At the last taking the sum of both the numbers
        
        a=str(l[0])+str(l[2])
        b=str(l[1])+str(l[3])
        s=int(a)+int(b)

        return s
        
