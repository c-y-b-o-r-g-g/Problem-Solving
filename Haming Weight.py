class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        binaryNum = bin(n)[-1:1:-1]
        for number in binaryNum:
            if number == '1':
                counter+=1        
        return counter
    