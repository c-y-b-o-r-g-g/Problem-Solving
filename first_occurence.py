import bython
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # search for occurence of first letter
        # if found : check next
        # if not equal? return to finding the occurence of first letter
        if (len(needle) > len(haystack)):
            return -1
        thisword = False
        indexes = []
        
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                indexes.append(i)
                
        for index in indexes:
            if index + len(needle) > len(haystack):
                continue
            for i in range(0, len(needle)):
                if haystack[index+i] != needle[i]:
                    thisword = False
                    break
                thisword = True
                
            if thisword == True:
                return index
        return -1
            
        
        
            
            
        
    print(strStr(0,"mississippi","issipi"))