class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        out = []
        product = 1
        for number in nums:
            product  = product * number
            print(product)
        # print(product)
        for number in nums:
            try:
                # print(product//number)
                out.append(product//number)
            except ZeroDivisionError:
                out.append(0)
        # print(out)
        return out
        
        
sol = Solution()
res = sol.productExceptSelf([-1,1,0,-3,3])
print(res)