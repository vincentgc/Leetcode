class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g,s = sorted(g), sorted(s)
        i,j = 0,0
        res = 0
        while i < len(g):
            if j >= len(s):
                break
            else:
                if s[j] >= g[i]:
                    res += 1
                    j += 1
                    i += 1
                else:
                    j += 1
        return res