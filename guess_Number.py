# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        g = guess(n)
        while (g !=0):
            if g<0:
                n-=1
            else:
                n+=1
            g = guess(n)
        return g