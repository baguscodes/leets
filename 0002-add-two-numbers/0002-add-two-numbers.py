# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Helper function to add two digits and return the sum and carry
        def addDigits(d1, d2, carry):
            total = d1 + d2 + carry
            return total % 10, total // 10

        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            digit_sum, carry = addDigits(val1, val2, carry)
            current.next = ListNode(digit_sum)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # If there's a carry at the end, create a new node with the carry
        if carry:
            current.next = ListNode(carry)

        return dummy_head.next

# Example usage:
# Create two linked lists representing 342 and 465 (in reverse order)
# l1 = 2 -> 4 -> 3
# l2 = 5 -> 6 -> 4
# The sum is 342 + 465 = 807, represented as 7 -> 0 -> 8 in the linked list.
