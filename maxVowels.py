class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        # count = []
        max = 0
        for i in range(len(s)-k+1):
            word = ""
            c = 0
            for j in range(i,i+k):
                word+=s[j].lower()
                if s[j] in vowels:
                    c+=1
            if c > max :
                max = c
            # count.append(c)
        # print(count)
        return max
                
            
            
        
        
sol = Solution()
res = sol.maxVowels("weallloveyou",7)