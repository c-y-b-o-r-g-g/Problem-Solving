class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = {
            
        }
        for i in range(len(s)):
            if s[i] not in letters.keys():
                letters[s[i]] = 1
            elif s[i] in letters.keys():
                letters[s[i]] +=1
        for key in letters.keys():
            if letters.get(key) ==1:
                return s.index(key)
        return -1
        
        
sol = Solution()
res = sol.firstUniqChar("aabb")
print(res)