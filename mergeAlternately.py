class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        for i in range(len(min(word1,word2,key=len))):
            output+=word1[i]
            output+=word2[i]
        if len(word1)!=len(word2):
            output+=max(word1,word2,key=len)[i+1:]
        return output
        
        
sol = Solution()
res = sol.mergeAlternately(word1 = "abc", word2 = "pqr")
print(res)