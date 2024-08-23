class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = bin(x)[2:]
        b = bin(y)[2:]
        if len(a) < len(b):
            a,b = b,a
        b = b.zfill(len(a))        
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count+=1
        return count
        
sol = Solution()
res = sol.hammingDistance(3,1)