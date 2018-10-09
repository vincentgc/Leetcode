class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return True
        if s == s[::-1]:
            return True
        else:
            for i in range(len(s)):
                tmp = s[:i] + s[i+1:]
                if tmp == tmp[::-1]:
                    return True
        return False