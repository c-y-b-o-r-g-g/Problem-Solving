class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        strings = [s1,s2,s3]
        # print(strings)
        l = len(max(s1,s2,s3,key=len))
        for i in range(l-1):
            if s1==s2==s3:
                return True
            longest = max(s1,s2,s3,key=len)
            place = strings.index(longest)
            longest = longest[:-1]
            print(longest)
            strings[place] = longest
            
            
            
        #     longest = longest[:len(longest)-1]
        # # print(longest)
        #     strings[i] = longest
        #     print(strings)
        
        
        
        # while not (s1==s2==s3):
        #     longest = max(s1,s2,s3,key = len)
        #     print(longest)
        #     i = strings.index(longest)
        #     i=0
        #     longest = longest[:len(longest)-1]
        #     strings[i] = longest
        # print(longest)
        # print(strings)
        
        
sol = Solution()
sol.findMinimumOperations( s1 = "abc", s2 = "abb", s3 = "ab")