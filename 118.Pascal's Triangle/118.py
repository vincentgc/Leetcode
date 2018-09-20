class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            res = []
        if numRows==1:
            res = [[1]]
        if numRows>=2:
            res = [[1],[1,1]]
        for i in range(2,numRows):
            tmp = [[0] for _ in range(i+1)]
            res.append(tmp)
            res[i][0] = 1
            res[i][-1] = 1
            for j in range(1,len(res[i])-1):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
                