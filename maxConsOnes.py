class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        counts = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            elif nums[i] == 0:
                counts.append(count)
                count = 0
        counts.append(count)
        return max(counts)
                
            
            
            
            
sol = Solution()
sol.findMaxConsecutiveOnes([1,0,1,1,0,1])