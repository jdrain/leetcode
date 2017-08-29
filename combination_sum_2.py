# https://leetcode.com/problems/combination-sum-ii/description/

"""
Accepted, but kind of hacky...
It would be nice to find a more organic way to avoid duplicates
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # init
        sols = []
        p_sols = []
        candidates.sort()
        for i in candidates:
            if i <= target:
                j = 0
                l = len(p_sols)
                while j < l:
                    tmp = p_sols[j][:]
                    tmp.append(i)
                    if sum(tmp) < target:
                        p_sols.append(tmp)
                    elif sum(tmp) == target and tmp not in sols:
                        sols.append(tmp)
                    j += 1
                tmp = [i]
                if i == target and tmp not in sols:
                    sols.append(tmp)
                elif i < target and tmp not in p_sols:
                    p_sols.append(tmp)
        return sols

if __name__ == '__main__':
    cand = [10,1,2,7,6,1,5]
    target = 8
    s = Solution()
    solution = s.combinationSum2(cand, target)
    print("Solution: ")
    print(solution)
