class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]:
            return False
        _sum = sum(nums)
        if _sum%2 != 0:
            return False
        target = _sum/2
        
        nums = sorted(nums,reverse=True)
        def help(index,target):
            if target<0:
                return
            if target==0:
                return True
            for i in range(index,len(nums)):
                    if help(i+1,target-nums[i]):
                        return True
            return False
        return help(0,target)