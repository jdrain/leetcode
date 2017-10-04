# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        i = 0
        j = len(heights)- 1
        A = min(heights) * (j - i + 1)
        while i < j:
            if heights[i] < heights[j]:
                i += 1
                if heights[i] > heights[i - 1]:
                    A = max(A, min(heights[i:j + 1]) * (j - i + 1))
            elif heights[j] < heights[i]:
                j -= 1
                if heights[j] > heights[j + 1]:
                    A = max(A, min(heights[i:j + 1]) * (j - i + 1))
            else:
                if heights[j - 1] < heights[i + 1]:
                    j -= 1
                    if heights[j] > heights[j + 1]:
                        A = max(A, min(heights[i:j + 1]) * (j - i + 1))
                else:
                    i += 1
                    if heights[i] > heights[i - 1]:
                        A = max(A, min(heights[i:j + 1]) * (j - i + 1))
        return A

if __name__ == '__main__':
    ht = [2,1,5,6,2,3]
    s = Solution()
    print(s.largestRectangleArea(ht))
