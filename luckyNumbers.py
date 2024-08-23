class Solution:
    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        for row in matrix:
            for number in row:
                print(number)
        
            
        
        
sol = Solution()
res = sol.luckyNumbers(matrix = [[3,7,8],[9,11,13],[15,16,17]])
print(res)