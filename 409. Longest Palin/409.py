class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            d[i] = d.get(i,0)+1
        res = 0
        flag = False
        for p in d.keys():
            if d[p] % 2 == 0:
                res += d[p]
            else:
                res += d[p]-1
                flag =True
        if flag:
            res += 1
        return res