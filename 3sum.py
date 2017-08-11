# https://leetcode.com/problems/3sum/description/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # edge cases
        if len(nums) < 3:
            return []

        # sort input
        nums.sort()

        # init
        k = len(nums) - 1
        sol = []

        while k >= 2:
            hi = k - 1
            lo = 0
            while lo < hi:
                s = nums[lo] + nums[hi] + nums[k]
                if s == 0:
                    sol.append[nums[lo],nums[hi],nums[k]]
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]
                else if s > 0:
                    hi -= 1
                else:
                    lo += 1
            k -= 1
        return sol
