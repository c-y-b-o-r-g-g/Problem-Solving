class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        import math
        if n == 0:
            return True
        
        if (math.log2(n) == int(math.log2(n))):
            return True
        return False
        # print(math.log2(int(3)))
        
    
sol = Solution()
res = sol.isPowerOfTwo(0)
print(res)