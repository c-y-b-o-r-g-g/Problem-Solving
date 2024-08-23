class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        a = 0
        b = 1
        for i in range (len(nums)):
            p1 = nums[a]
            p2 = nums[b]
            if p1 == p2 and b == a+1:
                b+=1
            elif p1!=p2:
                a+=1
                b+=1
            elif p1==p2 and b!= a+1:
                p2 = nums[b+1]
                p1 = nums[b]
                
                
        print(nums)
        
          
        