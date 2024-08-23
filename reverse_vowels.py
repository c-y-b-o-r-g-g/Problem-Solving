class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = ['a','e','i','o','u','A','E','I','O','U']
        vowels = []
        indexes = []
        s_list = list(s)
        for i in range(len(s)):
            if s[i] in chars:
                vowels.append(s[i])
                indexes.append(i)
        j = -1
        for i, index in enumerate(indexes):
            s_list[index] = vowels[-(i + 1)]
        
        return ''.join(s_list)
            
        
sol = Solution()
res = sol.reverseVowels("leetcode")
print(res)
