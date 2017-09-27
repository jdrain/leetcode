# https://leetcode.com/problems/n-queens/description/

import sys

"""
Given an integer n, output all configurations of n queens on
an nxn chess board where no queen is attacking another
"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        # init
        p_sols = [[[i for i in range(0,n)] for j in range(0,n)]]
        tmp_sols = []
        i = 0 # row count
        ct = 0 # curious...
        while i < n and p_sols:
            for p_sol in p_sols:
                for j in p_sol[i]:
                    tmp_sol = p_sol[:i]
                    tmp_sol.append(j)
                    for k in range(1, n-i): # eliminate invalid positions further down
                        tmp_sol.append([elem for elem in p_sol[i+k] if elem != j and elem != j+k and elem != j-k])
                        ct  += 1
                    tmp_sols.append(tmp_sol[:])
            p_sols = tmp_sols[:]
            del tmp_sols[:]
            i += 1

        print("\n basic op ran {} times...".format(ct))
        for sol in p_sols: # render each list as a string
            for j in range(0,len(sol)):
                tmp = sol[j]
                sol[j] = ''.join(['.' if k != sol[j] else 'Q' for k in range(0,n)])
        return p_sols

if __name__ == "__main__":
    n = int(sys.argv[1])
    S = Solution()
    s = S.solveNQueens(n)
    for i in range(0,len(s)):
        print("Solution no. {}:".format(i+1))
        for j in s[i]:
            print(j)
        print("\n")
