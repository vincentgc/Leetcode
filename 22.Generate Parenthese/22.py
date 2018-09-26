class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def help(left,right,tmp,res):
            if right<left:
                return
            if not right and not left:
                res.append(tmp)
                return
            if left:
                help(left-1,right,tmp+'(',res)
            if right:
                help(left,right-1,tmp+')',res)
        help(n,n,'',res)
        return res