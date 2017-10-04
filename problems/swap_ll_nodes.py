# swap ll nodes
# https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        else:
            final_head = head.next
            a = head
            b = a.next
            tmp = None

            while a != None:
                a.next = b.next
                b.next = a
                if tmp != None:
                    tmp.next = b
                tmp = a
                a = a.next
                if a != None and a.next != None:
                    b = a.next

            return final_head

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# testing
w = ListNode(0)
x = ListNode(1)
y = ListNode(2)
z = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)

w.next = x
x.next = y
y.next = z
z.next = d
d.next = e
e.next = f
f.next = g

s = Solution()
swapped = s.swapPairs(w)
tmp_node = swapped

while tmp_node != None:
    print(tmp_node.val)
    tmp_node = tmp_node.next
