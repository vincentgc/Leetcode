class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i,v in enumerate(s):
            if v not in d:
				#要考虑存储两个信息（数量和位置）
                d[v] = [1,i]
            else:
                d[v][0] += 1
        res = []
        for j in d.keys():
            if d[j][0] == 1:
                res.append(d[j][1])
        if len(res) > 0:
            res = sorted(res)
            return res[0]
        else:
            return -1