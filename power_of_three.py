class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        import math
        if n <= 0:
            return False
        
        # if (math.log2(n) == int(math.log2(n))):
        #     return True
        # return False
        if (math.log(n,3) == int(math.log(n,3))):
            return True
        return False
        # print(math.log(9,3))
        # print(math.log2(int(3)))
        
        
sol = Solution()
res = sol.isPowerOfThree(59049)
print(res)
