class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        b = s + t
        res = 0
        for i in b:
            res = res^ord(i)
        return chr(res)