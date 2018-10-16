class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0:
            return []
        res = []
        n,m= len(matrix),len(matrix[0])
        left,right,top,down = 0,m-1,0,n-1
        while left<=right and top<=down:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            #print res
            top += 1
            if top > down:
                break
            for i in range(top,down+1):
                res.append(matrix[i][right])
            #print res
            right -= 1
            if left > right:
                break
            for i in range(right,left-1,-1):
                res.append(matrix[down][i])
            #print res
            down -= 1
            for i in range(down,top-1,-1):
                res.append(matrix[i][left])
            #print res
            left += 1
        return res