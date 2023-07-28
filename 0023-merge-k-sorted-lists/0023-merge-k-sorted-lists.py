# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge_two_lists(l1, l2):
            dummy = ListNode(-1)
            current = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next

                current = current.next

            current.next = l1 or l2

            return dummy.next

        def merge_lists(left, right):
            if left == right:
                return lists[left]

            mid = (left + right) // 2
            return merge_two_lists(merge_lists(left, mid), merge_lists(mid + 1, right))

        if not lists:
            return None

        return merge_lists(0, len(lists) - 1)