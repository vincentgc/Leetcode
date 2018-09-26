class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        res = 0
        layer = 0
        flag = False
        for i in S:
            if i == '(':
                layer += 1
                flag = True
            else:
                layer -= 1
                if flag:
                    res += 2**layer
                    flag = False
        return res