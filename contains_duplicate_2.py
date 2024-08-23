class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # [1,2,3,1,2,3]
        
        
        for i in range(len(nums)//2):
            t1 = nums[i]
            indexes = []
            for j in range(i,len(nums)):
                if t1 == nums[j]:
                    indexes.append(j)
            print(indexes)
            for z in range(0,len(indexes)):
                for l in range(k,len(indexes)):
                    if abs(z-l) <=k:
                        # return True
                        print("Here")
            
        # return indexes
        # return False
        print("Not here")
        
        
        
        
        
        # indexes = []
        # t1 = nums[0]
        # for i in range(len(nums)):
        #     if nums[i] == t1:
        #         indexes.append(i)
        # if (abs(indexes[0] - indexes[1]))<=k:
        #     return True
        # return False
    
    
    
sol = Solution()
res = sol.containsNearbyDuplicate([1,2,3,1],3)
# print(res)