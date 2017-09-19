# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        digit_map = {"2":["a","b","c"],
                    "3":["d","e","f"],
                    "4":["g","h","i"],
                    "5":["j","k","l"],
                    "6":["m","n","o"],
                    "7":["p","q","r","s"],
                    "8":["t","u","v"],
                    "9":["w","x","y","z"]
                }

        combinations = []
        for d in digits:
            tmp = []
            if not combinations:
                for l in digit_map[d]:
                    combinations.append(l)
            else:
                for c in combinations:
                    for l in digit_map[d]:
                        tmp.append(c + l)
                combinations = tmp[:]
        return combinations

if __name__ == '__main__':
    s = Solution()
    digits = "23"
    print(s.letterCombinations(digits))
