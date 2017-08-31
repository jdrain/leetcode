# https://leetcode.com/problems/subsets/description/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sols = [[]]
        for i in nums:
            tmp_sols = sols[:]
            for j in tmp_sols:
                tmp = j[:]
                tmp.append(i)
                sols.append(tmp)
        return sols
