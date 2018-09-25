class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def isPattern(s,t):
            j = 0
            d1 = {}
            mode1 = []
            for i in s:
                if i not in d1:
                    d1[i] = j
                    j += 1
                mode1.append(d1[i])
            p = 0
            d2 = {}
            mode2 = []
            for v in t:
                if v not in d2:
                    d2[v] = p
                    p += 1
                mode2.append(d2[v])
            return mode1 == mode2
        res = []
        for i in words:
            if isPattern(i,pattern):
                res.append(i)
        return res