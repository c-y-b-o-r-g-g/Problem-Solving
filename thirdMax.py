class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        l = 0
        for number in nums:
            l+=1
        nums.sort()
        n = set(nums)
        n = list(n)
        n = n[::-1]
        print(n)
        l = len(n)
        if l>=3:
            return n[2]
        return n[0]
            
        


sol = Solution()
res = sol.thirdMax([-1,2,3])
print(res)