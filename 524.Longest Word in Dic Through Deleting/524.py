class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def help(s,w):
            n,m = len(s),len(w)
            i,j = 0,0
            while i<n and j<m:
                if s[i]==w[j]:
                    j+=1
                i+=1
            if j==m:
                return True
            else:
                return False
        d = sorted(d)
        maxLen = 0
        res = ''
        for w in d:
            if help(s,w):
                if maxLen < len(w):
                    maxLen = len(w)
                    res = w
        return res