class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        out = []
        out.append(0)
        sum = out[0]
        for i in range(len(gain)):
            sum+=gain[i]
            out.append(sum)
        return max(out)
    
    
sol = Solution()
res = sol.largestAltitude([-4,-3,-2,-1,4,3,2])
print(res)