class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
            result =[]
            for i in range(len(nums)+1):
                if i not in nums:
                    result.append(i)
            result.remove(0)
            return result
        
sol = Solution()
res = sol.findDisappearedNumbers([1,1])
print(res)