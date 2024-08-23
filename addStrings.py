class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        values = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        n1 = 0
        n2 = 0
        for number in num1:
            n1 = 10*n1 + values[number]
        
        for number in num2:
            n2 = 10*n2 + values[number]
        
        return str(n1+n2)
        
sol = Solution()
res = sol.addStrings(num1 = "11", num2 = "123")
print(res)