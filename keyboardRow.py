class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        
        res = []
        currentRow = 0
        appendFlag = False
        for word in words:
            lowerWord = word.lower()
            if lowerWord[0] in row1:
                currentRow = row1
            elif lowerWord[0] in row2:
                currentRow = row2
            else:
                currentRow = row3
            for letter in lowerWord:
                if letter not in currentRow:
                    appendFlag = False
                    break
                appendFlag = True
            if appendFlag == True:
                res.append(word)
        return res
        
        
sol = Solution()
res = sol.findWords(["adsdf","sfd"])
print(res)