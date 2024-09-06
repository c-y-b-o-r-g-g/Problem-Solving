class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if(m*n != len(original)):
            return []
        result = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(original[i*n+j])
            result.append(row)
        return result
        
        
        
sol = Solution()
res = sol.construct2DArray(original = [1,2,3,4], m = 2, n = 2)
print(res)