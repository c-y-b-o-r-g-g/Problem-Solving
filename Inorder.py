# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        
        def func(x):
            if x is None:
                return
            func(x.left)
            res.append(x.val)
            func(x.right)
        
        func(root)
        return res
            
            
            
        
        
        