class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d = {}
        j = 0
        mode1 = []
        _str = str.split()
        for i in _str:
            if i not in d.keys():
                d[i] = j
                j += 1
            mode1.append(d[i])
        d1 = {}
        p = 0
        mode2 = []
        for v in pattern:
            if v not in d1:
                d1[v] = p
                p += 1
            mode2.append(d1[v])
        return mode1 == mode2