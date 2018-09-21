class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        if rowIndex >= 2:
            res = [1,1]
        for i in range(2,rowIndex+1):
            if len(res) < i+1:
                res.append(1)
            tmp = [i for i in res]
            for j in range(1,len(res)-1):
                res[j] = tmp[j-1]+tmp[j]
        return res