class Solution:
    def addDigits(self, num: int) -> int:
        myNum = str(num)
        while(len(myNum))>1:
            sum=0
            for number in myNum:
                sum+=int(number)
            myNum = str(sum)
        return int(myNum)
    
    
sol = Solution()
res = sol.addDigits(0)
print(res)