# https://leetcode.com/problems/add-two-numbers/#/description

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

        - start with a new list of one node with val = 0
        - look at both head nodes and add them
            + if sum greater than 9 carry over to a new node
            + else just link a node with val = 0
        - repeat until lists are empty
        """

        listOneCurrentNode = l1
        listTwoCurrentNode = l2
        solution = ListNode(0)
        currentSolutionNode = solution
        tmp = 0

        while listOneCurrentNode != None or listTwoCurrentNode != None:
            # add both
            if listOneCurrentNode != None:
                tmp += listOneCurrentNode.val
                listOneCurrentNode = listOneCurrentNode.next
            if listTwoCurrentNode != None:
                tmp += listTwoCurrentNode.val
                listTwoCurrentNode = listTwoCurrentNode.next
            # update tmp and the solution list
            if currentSolutionNode.val + tmp > 9:
                currentSolutionNode.val = (currentSolutionNode.val + tmp) % 10
                currentSolutionNode.next = ListNode((currentSolutionNode.val + tmp) / 10)
                currentSolutionNode = currentSolutionNode.next
            else:
                currentSolutionNode.val = currentSolutionNode.val + tmp
                currentSolutionNode.next = ListNode(0)
                currentSolutionNode = currentSolutionNode.next
            tmp = 0

        # remove the last node/display the result
        tmp = solution
        tmpSolution = ListNode(solution.val)
        while tmp.next != None:
            if tmp.next.next == None and tmp.next == 0:
                tmp.next = None
            tmp = tmp.next

        return tmpSolution
