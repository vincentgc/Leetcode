class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
		#重点在于两个矩形的两条边都要有交叉
        row1 = [rec1[0],rec1[2]]
        row2 = [rec2[0],rec2[2]]
        col1 = [rec1[1],rec1[3]]
        col2 = [rec2[1],rec2[3]]
        if row1[0] <= row2[0]:
            left,right = row1,row2
        else:
            left,right = row2,row1
        if col1[0] <= col2[0]:
            bottom,up = col1,col2
        else:
            bottom,up = col2,col1
        overlap1 = False
        overlap2 = False
        if right[1]-left[0] < (left[1]-left[0])+(right[1]-right[0]):
            overlap1 = True
        if up[1]-bottom[0] < (bottom[1]-bottom[0])+(up[1]-up[0]):
            overlap2 = True
        return overlap1 and overlap2