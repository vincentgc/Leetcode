class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
		#从行和列两个方向进行对角线扫描
        M, N = len(matrix),len(matrix[0])
        for i in range(M):
            j = 0
            pivot = matrix[i][j]
            i += 1
            j += 1
			#对角线扫描
            while i < M and j < N:
                if matrix[i][j] != pivot:
                    return False
                i += 1
                j += 1
        for j in range(N):
            i = 0
            pivot = matrix[i][j]
            i += 1
            j += 1
            while i < M and j < N:
                if matrix[i][j] != pivot:
                    return False
                i += 1
                j += 1
        return True