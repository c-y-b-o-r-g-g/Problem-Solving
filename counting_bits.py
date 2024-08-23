class Solution:
    def countBits(self, n: int) -> list[int]:
        binary = bin(n)
        binary = binary[2:]
        counter = 0
        for number in binary:
            if number ==1:
                counter+=1
        return counter
        
sol = Solution()
res = sol.countBits(4)
print(res)
 