# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: list[ListNode]) -> bool:
        passed = []
        for i in range(len(head)):
            passed.append(i)
        print(passed)
        if head.next in passed:
            print("Loop")
        
            
sol = Solution()
sol.hasCycle(head = [1,2])            