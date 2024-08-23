class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        for number in nums1:
            index = nums2.index(number)
            found = False
            for i in range(index, len(nums2)):
                if nums2[i] > number:
                    result.append(nums2[i])
                    found = True
                    break
            if not found:
                result.append(-1)
        # print(result[:-1])
        return result
            
        
sol = Solution()
res = sol.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4])
print(res)
