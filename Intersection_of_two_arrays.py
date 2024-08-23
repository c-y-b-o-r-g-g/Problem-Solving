class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        inter = []
        for number in nums1:
            if number in nums2:
                nums2.remove(number)
                if number not in inter:
                    inter.append(number)
                
        return inter
       

sol = Solution()
res = sol.intersect(nums1 = [1,2,2,1], nums2 = [2,2])
print(res)
