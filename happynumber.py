class Solution:
    def isHappy(self, n: int) -> bool:
        sum=0
        while len(n) != 1:
            while n != 0 or sum !=0:
                sum += pow((n%10),2)
                n = n//10
    
        print(sum)    
            
    
        
        
sol = Solution()
res = sol.isHappy(19)
# print(res)