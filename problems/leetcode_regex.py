class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        re_ls = []
        s_ls = []

        # parse the regex
        i = 0
        j = 0
        while i < len(p):
            re_ls.append([p[i],1])
            i += 1
            if i < len(p) and p[i]=="*":
                re_ls[j][1] = 0
                i += 1
            j += 1

        print(re_ls)

    def recursiveRegex(re_ind, str_ind):
        # base case
        if (re_ind < len(re_ls) - 1) and (str_ind < len(s) - 1):
            # is the current regex quantifier 1 or *?
            if 

s = Solution()
s.isMatch("aab", "c*a*b")
