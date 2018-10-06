class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for i in range(l/2):
            matrix[i],matrix[l-i-1] = matrix[l-i-1],matrix[i]
        for p in range(l):
            for v in range(p):
                matrix[p][v],matrix[v][p] = matrix[v][p],matrix[p][v]
        