import unittest

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        # Create a linked list with duplicates
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(2)

        # Call the function
        remove_duplicates(head)

        # Check the result
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 2)
        self.assertIsNone(head.next.next)

if __name__ == '__main__':
    unittest.main()