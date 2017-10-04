# https://leetcode.com/problems/trapping-rain-water/description/

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s = 0
        delta =  0
        stack = []
        for i in range(1, len(height)):
            delta = height[i] - height[i - 1]
            if delta < 0: # drop
                stack.append([i,delta])
            while delta > 0 and len(stack) != 0: # jump
                if delta >= -(stack[-1][1]):
                    s += -(stack[-1][1])*(i - stack[-1][0])
                    delta += stack[-1][1]
                    del stack[-1]
                else:
                    s += delta*(i-stack[-1][0])
                    stack[-1][1] += delta
                    delta = 0
        return s
