class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        exist = set()
        while n!=1:
            if n in exist:
                return False
            else:
                exist.add(n)
                tmp = n
                res = 0
                while tmp > 0:
                    res += (tmp%10)**2
                    tmp = tmp/10
                n = res
        return True