class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        out = [None]*len(score)
        l = len(score)
        strs = ["Gold Medal","Silver Medal","Bronze Medal"]
        c = 0
        for i in range(l):
            m = max(score)
            index = score.index(m)
            if c<3:
                out[index] = strs[c]
                c+=1
            else:
                out[index] = str(i+1)
            score[index] = -1
        return out
        
        
        
sol = Solution()
res = sol.findRelativeRanks(score = [10,3,8,9,4])
print(res)