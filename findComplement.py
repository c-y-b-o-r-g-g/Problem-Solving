class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        new = ""
        for i in range(len(binary)):
            if binary[i] == "1":
                new+="0"
            else:
                new+="1"
        new = new[::-1]
        sum = 0
        for i in range(len(new)):
            if new[i] == "1":
                sum+= 2**i
        return sum
        
        
        
sol = Solution()
sol.findComplement(4)
