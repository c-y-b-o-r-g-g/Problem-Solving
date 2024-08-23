class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(0,len(nums)):
            count = 0
            for j in range (i, len(nums)):
                if nums[i] == nums[j]:
                    count+=1
            if count >=2:
                return True
        return False
            
    
    print(containsDuplicate(0,[1,2,3,4]))
            
    