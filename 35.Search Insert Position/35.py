class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
		#注意边界条件
        l,r= 0,len(nums)-1
        if target > nums[-1]:
            return len(nums)
        while l<r:
            if (r-l)==1 and target>nums[l] and target<=nums[r]:
                return r
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid
            elif nums[mid]==target:
                return mid
            else:
                r = mid
        return l