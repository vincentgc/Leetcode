class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row,col = len(nums),len(nums[0])
        if row * col != r * c:
            return nums
        else:
			#先定义好result的大小（这样速度比较慢，也可以动态向result里添加元素）
            result = [[[0] for i in range(c)] for j in range(r)]
            for i in range(row):
                for j in range(col):
                    total = i*col + j
                    r_new = total // c
                    c_new = total - r_new * c
                    result[r_new][c_new] = nums[i][j]
            return result