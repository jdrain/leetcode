# spiral matrix problem
# https://leetcode.com/problems/spiral-matrix/description/

import random

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ls = []
        i = 0
        n = len(matrix)
        m = len(matrix[0])

        if min(m,n) % 2 == 0:
            stop = min(m,n) / 2
        else:
            stop = (min(m,n) + 1) / 2

        while i < stop:
            out = i
            down = i
            ls.append(matrix[down][out])

            while out < m - i - 1:
                out += 1
                ls.append(matrix[down][out])

            while down < n - i - 1:
                down += 1
                ls.append(matrix[down][out])

            while out > i:
                out -= 1
                ls.append(matrix[down][out])

            while down > i + 1:
                down -= 1
                ls.append(matrix[down][out])

            i += 1

        return ls

def pprint_2d_matrix(matrix):
    for i in matrix:
        print(i)

if __name__ == '__main__':
    rx = random.randint(1,6)
    ry = random.randint(1,6)
    rand_matrix = [[random.randint(0,12) for i in range(0,rx)] for i in range(0,ry)]
    s = Solution()
    sol = s.spiralOrder(rand_matrix)

    print("randomized matrix: ")
    pprint_2d_matrix(rand_matrix)

    print("spiral order: {}".format(sol))
