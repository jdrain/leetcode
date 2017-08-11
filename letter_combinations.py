# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution(object):
    nums = {"2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
            "0":[" "]
           }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        i = 0
        ss = set()
        self.recursiveCombine(i, digits, "", ss)
        return (list(ss))

    def recursiveCombine(self, current_ind, digits, combo_str, solution_set):
        if current_ind < len(digits):
            for i in self.nums[digits[current_ind]]:
                self.recursiveCombine(current_ind + 1, digits, combo_str + i, solution_set)
        else:
            if combo_str not in solution_set:
                solution_set.add(combo_str)
