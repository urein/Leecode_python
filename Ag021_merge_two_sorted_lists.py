"""
Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: l1 = [], l2 = []
Output: []

Input: l1 = [], l2 = [0]
Output: [0]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, ph1:ListNode, ph2:ListNode):
        # recursion exit
        if ph1 is None or ph2 is None:
            return ph2 if ph1 is None else ph1
        # recursion
        if ph1.val <= ph2.val:
            ph1.next = self.merge_two_lists(ph1.next, ph2)
            return ph1
        else:
            ph2.next = self.merge_two_lists(ph1, ph2.next)
            return ph2


if __name__ == '__main__':
    s = Solution()
    l1_n1 = ListNode(1)
    l1_n2 = ListNode(2)
    l1_n3 = ListNode(4)

    l1_n1.next = l1_n2
    l1_n2.next = l1_n3

    l2_n1 = ListNode(1)
    l2_n2 = ListNode(3)
    l2_n3 = ListNode(4)

    l2_n1.next = l2_n2
    l2_n2.next = l2_n3

    r = s.merge_two_lists(l1_n1, l2_n1)



