class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 0
        for i in range(1, num//2+1):
            if num%i == 0:
                sum+=i
        if sum == num:
            return True
        return False
        
        
sol = Solution()
res = sol.checkPerfectNumber(28)
print(res)