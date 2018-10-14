class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        
        def isPal(s):
            return s == s[::-1]
        def help(s, path, res):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s)+1):
                if isPal(s[:i]):
                    help(s[i:], path+[s[:i]], res)
        
        help(s,[],res)
        return res