class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for i in s:
            d[i] = d.get(i,0)+1
        sort_d = sorted(d.items(),key=lambda x:x[1],reverse=True)
        res = ''
        for p in sort_d:
            res += p[0]*p[1]
        return res