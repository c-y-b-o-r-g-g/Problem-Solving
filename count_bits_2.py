class Solution:
    def countBits(self, n: int) -> list[int]:
        count = []
        for i in range(0,n+1):
            counter = 0
            numString = bin(i)[2:]
            for j in range(len(numString)):
                if numString[j] == "1":
                    counter+=1
            count.append(counter)
        # print(count)
        return count
                    
                
            
        
        
        
sol = Solution()
res = sol.countBits(5)