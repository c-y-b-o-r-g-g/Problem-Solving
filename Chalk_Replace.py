class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        students_number = len(chalk)
        current_student = 0
        
        while True:
            if k< chalk[current_student]:
                break
            
            k -= chalk[current_student]
            current_student = (current_student+1)%students_number
        return current_student
        
        
        
sol = Solution()
res = sol.chalkReplacer(chalk = [3,4,1,2], k = 25)
print(res)