class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l1 = []
        l2 = []
        for i in range(len(s)):
            l1.append(s[i])
            l2.append(t[i])
        l1.sort()
        l2.sort()
        if l1 != l2:
            return False
        else:
            return True