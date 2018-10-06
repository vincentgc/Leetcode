class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        sort_p = sorted(points,key=lambda x: x[0])
        stack = [sort_p[0]]
        for i in sort_p:
            if i[0] <= stack[-1][1]:
                stack[-1][0],stack[-1][1] = max(i[0],stack[-1][0]),min(i[1],stack[-1][1])
            else:
                stack.append(i)
        return len(stack)