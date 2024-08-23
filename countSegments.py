class Solution:
    def countSegments(self, s: str) -> int:
        n = len(s)
        i = 0
        c = 0
        while i <n:
            while (i<n and s[i] ==" "):
                i+=1
                count = False
            while (i<n and s[i] !=" "):
                i+=1
                count = True
            if count:
                c+=1
            i+=1
        return(c)

            
            
sol = Solution()
res = sol.countSegments("Hello, my name is John")
print(res)
