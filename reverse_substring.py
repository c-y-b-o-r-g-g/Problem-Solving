class Solution:
    def reverseParentheses(self, s: str) -> str:
        tempstring = []
        for i in range(len(s)):
            if s[i] == "(":
                while(s[i] != ")"):
                    tempstring.append(s[i])
                    i+=1
                    if s[i] =="(":
                        tempstring.clear()
                    
        tempstring = tempstring[1:]
        tempstring.reverse()
        print(tempstring)
        
        
sol = Solution()
sol.reverseParentheses("(gehad)()")