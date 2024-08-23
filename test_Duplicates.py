# Test Case 1: No duplicates in the linked list
# Input: 1 -> 2 -> 3 -> 4 -> 5
# Output: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
solution = Solution()
result = solution.deleteDuplicates(head)
# Expected Output: 1 -> 2 -> 3 -> 4 -> 5

# Test Case 2: Duplicates at the beginning of the linked list
# Input: 1 -> 1 -> 2 -> 3 -> 4 -> 5
# Output: 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
solution = Solution()
result = solution.deleteDuplicates(head)
# Expected Output: 2 -> 3 -> 4 -> 5

# Test Case 3: Duplicates in the middle of the linked list
# Input: 1 -> 2 -> 2 -> 3 -> 4 -> 5
# Output: 1 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
solution = Solution()
result = solution.deleteDuplicates(head)
# Expected Output: 1 -> 3 -> 4 -> 5

# Test Case 4: Duplicates at the end of the linked list
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 5
# Output: 1 -> 2 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(5)
solution = Solution()
result = solution.deleteDuplicates(head)
# Expected Output: 1 -> 2 -> 3 -> 4

# Test Case 5: Empty linked list
# Input: None
# Output: None
head = None
solution = Solution()
result = solution.deleteDuplicates(head)
# Expected Output: None