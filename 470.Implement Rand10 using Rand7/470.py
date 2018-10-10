class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        res = 11
        while res>10:
            res = (rand7()-1)*7+rand7()
        return res