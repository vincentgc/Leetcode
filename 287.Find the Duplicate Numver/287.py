 class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0,len(nums)-1
        mid = (l+r)/2
        while r-l > 1:
            count = 0
            for k in nums:
                if k > mid and k <= r:
                    count += 1
            if count > r - mid:
                l = mid
            else:
                r = mid
            mid = (l+r)/2
        return r
                   