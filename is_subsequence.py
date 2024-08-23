class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # search for s in t
        for letter in s:
            if letter not in t:
                return False
        return True
    
    