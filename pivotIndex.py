class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            start_sum = 0
            end_sum = 0
            for j in range(i):
                start_sum+=nums[j]
                print(nums[j])
            for j in range(-1,i-1,-1):
                end_sum+=nums[j]
                print(nums[j])
            if start_sum == end_sum:
                print(i)
            print("=========")
        
        
sol = Solution()
res = sol.pivotIndex([1,7,3,6,5,6])