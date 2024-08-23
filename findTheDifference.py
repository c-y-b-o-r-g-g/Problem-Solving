class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # ss = []
        # tt = []
        # for character in s:
        #     ss.append(character)
        # for character in t:
        #     tt.append(character)
        # ss.sort()
        # tt.sort()    
        # ss = set(ss)
        # tt = set(tt)
        
        # result = (max(ss,tt,key=len) - min(ss,tt,key=len))
        # # print(''.join(result))
        # return ''.join(result)
        
        
        
        chars = {}
        
        for char in s:
            chars[char] = "s"
        # print(chars)
        for char in t:
        
        
        
        # print(ss)
        # print(tt)
        
        
        
sol = Solution()
res = sol.findTheDifference("a", t = "aa")
print(res)

