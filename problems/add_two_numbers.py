# https://leetcode.com/problems/add-two-numbers/
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # make a new list to store the result
        listThreeHead = ListNode(0)
        l3 = listThreeHead
        remainder = 0
        while l1 or l2 or remainder > 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            val3 = val1 + val2 + remainder
            remainder = 0
            # check whether or not we need to carry the 1
            if val3 >= 10:
                val3 = val3 % 10
                remainder = 1
            l3.val = val3
            if l1 or l2 or remainder > 0:
                l3.next = ListNode(0)
                l3 = l3.next
        return listThreeHead
