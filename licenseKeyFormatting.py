class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-","").upper()
        result = []
        start = 0
        for i in range(len(s)):
            for j in range(start,start+k):
                result.append(s[j])
            result.append("-")
            start+=k
        print(result)
                
            
            
                
        
        
        
                
sol = Solution()
sol.licenseKeyFormatting(s = "5F3Z-2e-9-w", k = 4)