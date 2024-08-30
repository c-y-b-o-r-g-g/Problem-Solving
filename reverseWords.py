class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words.reverse()
        out = ""
        # print(words)
        for word in words:
            if word !="" and word!=" ":
                out+=word
                out+=" "
        return out.strip()
        

sol = Solution()
res = sol.reverseWords("a good   example")
print(res)
