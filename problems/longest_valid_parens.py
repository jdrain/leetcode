# https://leetcode.com/problems/longest-valid-parentheses/description/

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack= []
        l = 0
        m = 0
        for i in s:
            if i == "(":
                stack.append(i)
                l += 1
            else:
                if s[len(s)-1] == "(":
                    del stack[-1]
                    l += 1
                else:
                    if l > m:
                        m = l - len(stack)
                    l = 0
        return m
