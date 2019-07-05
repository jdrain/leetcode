# https://leetcode.com/problems/zigzag-conversion/

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0 or numRows == 1:
            return s
        
        result = ""    
        for row in range(0, numRows):
            down = 2 * (numRows - row) - 2
            up = 2 * row
            pointer = row
            goingDown = not down == 0
            while pointer <= len(s) - 1:
                result += s[pointer]
                pointer += down if goingDown else up
                goingDown = (not goingDown or up == 0) and not down == 0
        return result
