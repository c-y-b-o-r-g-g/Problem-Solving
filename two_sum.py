class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        si = 0
        ei = -1
        start = nums[si]
        end = nums[ei]
        while (start + end != target):
            start = nums[si]
            end = nums[ei]
            print(end)
            if start+end > target:
                ei-=1
            elif start+end < target:
                si +=1
        return [si,len(nums)+ei]
    
    
    
    print(twoSum(0,[-1,-2,-3,-4,-5],-8))