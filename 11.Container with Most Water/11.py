class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right = 0,len(height)-1
        _max = 0
        while left < right:
            l,r = height[left],height[right]
            if l < r:
                area = (right-left) * l
                while l >= height[left]:
                    left += 1
            else:
                area = (right-left) * r
                while r>=height[right] and right:
                    right -= 1
            _max = max(_max,area)
        return _max