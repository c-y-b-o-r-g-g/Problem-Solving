class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] < 9:
            digits[-1] +=1
        else:
            for i in range(len(digits)-1, -1, -1):
                if digits[i] < 9:
                    digits[i] += 1
                    break
                else:
                    digits[i] = 0
                    if i == 0:
                        digits.insert(0, 1)
                
        
x = [1,2,3]
sol = Solution()
sol.plusOne(x)
print(x)