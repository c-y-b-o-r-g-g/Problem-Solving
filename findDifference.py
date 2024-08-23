class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        hash1_set = set(nums1)
        hash2_set = set(nums2)
        out = [[],[]]
        
        for number in hash1_set:
            if number not in hash2_set:
                out[0].append(number)
        for number in hash2_set:
            if number not in hash1_set:
                out[1].append(number)
        return out
        
sol = Solution()
res = sol.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2])
print(res)