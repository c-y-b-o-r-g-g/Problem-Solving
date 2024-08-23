class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        l = len(nums)
        for number in nums:
            if number == val:
                # nums.remove(number)
                # nums.remove(number)
                nums.remove(val)
            else:
                k+=1
        print(nums)
        print(k)
        return k
        
    
    removeElement(0,[3,2,2,3,3],3)
    
    