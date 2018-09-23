class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
		#转化为数字的比较
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