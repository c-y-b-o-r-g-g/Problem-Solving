class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        temp = {}
        for number in arr:
            if number in temp:
                temp[number] +=1
            else:
                temp[number] = 1
        return (len(temp.values()) == len(set(temp.values())))
        
        
sol = Solution()
res = sol.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
print(res)