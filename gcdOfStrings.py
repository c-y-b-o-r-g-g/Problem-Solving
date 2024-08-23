class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ""
        
        start = str1[0]
        for i in range(len(min(str1,str2,key=len))):
            if str1[i] == str2[i]:
                if i != 0 and str2[i] == start:
                    break
                gcd+=str1[i]
            else:
                break
        
        if gcd == "":
            return gcd
        
        # print(max(str1,str2,key=len) / min(str1,str2,key=len))
        n = len(max(str1,str2,key=len)) // len(min(str1,str2,key=len))
        # print(n)
        
        if max(str1,str2,key=len) == min(str1,str2,key=len)*n:
            return min(str1,str2,key=len)
        
        l1 = len(str1)//len(gcd)
        l2 = len(str2)//len(gcd)
        comp1 = gcd*l1
        comp2 = gcd*l2
        if comp1 == str1 and comp2 == str2:
            return gcd
        return ""
        
        
            
        


sol = Solution()
res = sol.gcdOfStrings(str1 = "ABABABAB", str2 = "ABAB")
print(res)