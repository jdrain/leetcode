# https://leetcode.com/problems/n-queens-ii/description/

import sys
import matplotlib.pyplot as plt

"""
given an integer n, return the number of distinct solutions to the n queens problem
"""

class Solution(object):
    def totalNQueens(self, n, get_complexity=False):
        """
        :type n: int
        :rtype: int
        """
        # init
        p_sols = [[[i for i in range(0,n)] for j in range(0,n)]]
        tmp_sols = []
        i = 0 # row count
        ct = 0
        while i < n and p_sols:
            for p_sol in p_sols:
                for j in p_sol[i]:
                    tmp_sol = p_sol[:i]
                    tmp_sol.append(j)
                    for k in range(1, n-i): # eliminate invalid positions further down
                        tmp_sol.append([elem for elem in p_sol[i+k] if elem != j and elem != j+k and elem != j-k])
                        ct += 1
                    tmp_sols.append(tmp_sol[:])
            p_sols = tmp_sols[:]
            del tmp_sols[:]
            i += 1

        if get_complexity:
            return ct
        else:
            return len(p_sols)

if __name__ == "__main__":
    n = int(sys.argv[1])
    S = Solution()
    if len(sys.argv) >= 3 and sys.argv[2] == "--plot":
        n_ls = [i for i in range(0,n+1)]
        if len(sys.argv) >= 4 and sys.argv[3] == "--comp":
            s_ls = [S.totalNQueens(i, True) for i in n_ls]
            plt.plot(n_ls, s_ls, 'ro')
            plt.xlabel("Input size")
            plt.ylabel("Basic operations")
            plt.title("Basic Operations vs Input Size")
        else:
            s_ls = [S.totalNQueens(i) for i in n_ls]
            plt.plot(n_ls, s_ls, 'ro')
            plt.xlabel("Input size")
            plt.ylabel("Number of solutions")
            plt.title("Solutions vs Input Size")
        plt.show()
    else:
        s = S.totalNQueens(n)
        print("\nUnique solutions for {}x{} board: {}".format(n,n,s))
