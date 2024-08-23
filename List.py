# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

    tempNode = head
    counter = 0
    duplicates = []
    while tempNode.next != None:
        tempNode = tempNode.next
        duplicates.append(tempNode.val)
        counter = counter + 1

    tempNode = head
    while tempNode != None:
        if tempNode.val in duplicates:
            tempNode = tempNode.next

