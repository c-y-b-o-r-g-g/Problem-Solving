class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maximum = max(candies)
        res = [None]*len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maximum:
                res[i] = True
            else:
                res[i] = False
        # print(res)
        return res
        
sol = Solution()
res = sol.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3)
print(res)