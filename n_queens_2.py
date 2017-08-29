# https://leetcode.com/problems/n-queens-ii/description/

"""
given an integer n, return the number of distinct solutions to the n queens problem
"""

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # init
        p_sols = [[[i for i in range(0,n)] for j in range(0,n)]]
        tmp_sols = []
        i = 0 # row count
        while i < n and p_sols:
            for p_sol in p_sols:
                for j in p_sol[i]:
                    tmp_sol = p_sol[:i]
                    tmp_sol.append(j)
                    for k in range(1, n-i): # eliminate invalid positions further down
                        tmp_sol.append([elem for elem in p_sol[i+k] if elem != j and elem != j+k and elem != j-k])
                    tmp_sols.append(tmp_sol[:])
            p_sols = tmp_sols[:]
            del tmp_sols[:]
            i += 1
        return len(p_sols)
