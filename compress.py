class Solution:
    def compress(self, chars: list[str]) -> int:
        s = ""
        current = chars[0]
        count = 0
        for i in range(len(chars)):
            if chars[i] == current:
                count+=1
            elif chars[i] != current:
                if count==1:
                    s+= chars[i]
                else:
                    # s+= chars[i]
                    s+= current
                    s+= str(count)
                print(s)
                current = chars[i]
                count = 1
            # print(count)
        
        
        
sol = Solution()
res = sol.compress(["a","a","b","b","c","c","c"])