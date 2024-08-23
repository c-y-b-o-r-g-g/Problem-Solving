class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        minword = min(strs, key=len)
        if minword=="":
            return prefix
        if len(strs) == 1:
            return strs[0]
        for letter in minword:
            index = minword.index(letter)
            strs.remove(strs.index(minword))
            for word in strs:
                if word[index] == letter:
                    prefix+=letter
        # print(prefix)
        return prefix
    print(longestCommonPrefix(0,["flower","flow","flight"]))