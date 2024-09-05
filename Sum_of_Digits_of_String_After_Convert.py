class Solution:
    def getLucky(self, s: str, k: int) -> int:
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        result = ""
        for letter in s:
            result += str(letters.index(letter)+1)
        
        sum=0
        for i in range(0,k):
            sum=0
            for number in result:
                sum += int(number)
            result = str(sum)
        # print(result)
        return int(result)
            
        
        
        
        
        
sol = Solution()
res = sol.getLucky(s = "leetcode", k = 2)