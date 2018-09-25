class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]
        if nums[0]!=nums[1]:
            return nums[0]
        l,r = 0,len(nums)-1
        mid = (l+r)/2
        if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
            return nums[mid]
        if len(nums[l:mid])%2==1:
            if nums[mid]==nums[mid-1]:
                return self.singleNonDuplicate(nums[mid+1:])
            if nums[mid]==nums[mid+1]:
                return self.singleNonDuplicate(nums[:mid])
        else:
            if nums[mid]==nums[mid-1]:
                return self.singleNonDuplicate(nums[:mid-1])
            if nums[mid]==nums[mid+1]:
                return self.singleNonDuplicate(nums[mid:])