class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = s.split(' ')
        res = ''
        for w in word:
            w = w[::-1]
            res += w
            res += ' '
        return res[:-1]