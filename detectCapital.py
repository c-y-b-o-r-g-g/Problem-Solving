class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)==1:
            return True
        
        if word[0].isupper():
            
            if word[1].isupper():
                for i in range (2,len(word)):
                    if word[i].islower():
                        return False
                return True
            elif word[1].islower():
                for i in range(2,len(word)):
                    if word[i].isupper():
                        return False
                return True
        elif word[0].islower():
            for i in range(1,len(word)):
                if word[i].isupper():
                    return False
        return True
       
                    
        
        
        
    # All letters in this word are capitals, like "USA".
    # All letters in this word are not capitals, like "leetcode".
    # Only the first letter in this word is capital, like "Google".

    # case 1 
        
        
sol = Solution()
res = sol.detectCapitalUse("FlaG")
print(res)