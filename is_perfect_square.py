class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        import math
        root = math.sqrt(num)
        if root == int(root):
            return True
        return False