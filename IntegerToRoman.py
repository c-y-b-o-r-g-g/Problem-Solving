class Solution:
    def intToRoman(self, num: int) -> str:
        romans = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        result = ""
        
        for value,symbol in romans:
            while num >= value:
                result += symbol
                num-=value
        return result
        
        
        # Selecting Each Number with its place
        # multiple = 1
        # for i in range(len(str(num))):
        #     digit = (num % 10) * multiple
        #     num = num //10
        #     multiple *=10
        #     # print(digit)
        
        
        
        # converting number to roman
        
            
            
            
            
sol = Solution()
res = sol.intToRoman(3749)
print(res)