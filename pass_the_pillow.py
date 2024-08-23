class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        counter = 1
        up = True
        
        
        for i in range(time):
            if counter == 0:
                up = True
            elif counter == n:
                up = False
            if up == True:
                counter+=1
            elif up == False:
                counter-=1
            # print(counter)
        return counter
        
sol = Solution()
res = sol.passThePillow(18,38)
print(res)