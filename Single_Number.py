class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dup = []
        for i in range(len(nums)):
            if nums[i] in dup:
                dup.remove(int(nums[i]))
            else:
                dup.append(int(nums[i]))
            
        return dup[0]
    
    singleNumber(0,[1,2,1,2])