class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        count = 0
        for rows in range(len(grid)):
            for columns in range(len(grid[0])):
                # print(grid[rows][columns],end=" ")
                if grid[rows][columns] == 1:
                    # Check left
                    if columns == 0 or grid[rows][columns-1] == 0:
                        count += 1
                    # Check right
                    if columns == len(grid[0])-1 or grid[rows][columns+1] == 0:
                        count += 1
                    # Check top
                    if rows == 0 or grid[rows-1][columns] == 0:
                        count += 1
                    # Check bottom
                    if rows == len(grid)-1 or grid[rows+1][columns] == 0:
                        count += 1
        return count
            # print("\n")
        
        
sol = Solution()
sol.islandPerimeter([[1,0]])