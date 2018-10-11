class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            tmp = ''.join(sorted(s))
            if tmp not in d:
                d[tmp] = [s]
            else:
                d[tmp].append(s)
        res = []
        for i in d:
            res.append(d[i])
        return res
                