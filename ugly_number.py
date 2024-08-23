class Solution:
    def isUgly(self, n: int) -> bool:
        nums = [1,2,3,5]
        # for number in nums:
        #     res = n/number
        #     if res in nums:
        #         return True
        #     elif res/number in nums:
        #         return True
        # return False
        for number in nums and n!=0:
            if n/number in nums:
                return True
            n = n/number
        return False
                
            
        
    
    
sol = Solution()
res = sol.isUgly(16)
print(res)