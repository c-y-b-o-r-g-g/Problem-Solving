class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                # count+=1
                flowerbed[i] = "-1"
        # return count == n
        print(flowerbed)
                
            
        
sol = Solution()
res = sol.canPlaceFlowers(flowerbed = [1,0,0,0,0,1], n = 2)
# print(res)