# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1= head
        while temp1 is not None and temp1.next is not None:
            if temp1.val == temp1.next.val:
                temp1.next = temp1.next.next
            else:
                temp1 = temp1.next
        return head
    
    
            

        
        