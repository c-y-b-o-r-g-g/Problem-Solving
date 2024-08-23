class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        averages = []
        for i in range(len(nums)-k+1):
            sum = 0
            for j in range(i,i+k):
                sum+=nums[j]
            averages.append(sum/k)
        return max(averages)
        
sol = Solution()
res = sol.findMaxAverage(nums = [5], k = 1)
print(res)