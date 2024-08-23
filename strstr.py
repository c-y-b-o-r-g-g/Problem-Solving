class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index= 0
        flag = True
        for i in range(0,len(haystack)):
            if haystack[i] == needle[index]:
                index+=1
                for j in range (i+1, len(needle)):
                    if haystack[j] != needle[index]:
                        flag = False
                        break
                    index+=1

            if flag ==False:
                break


        return index

    print(strStr("gehad","gehadkhaled","adk"))