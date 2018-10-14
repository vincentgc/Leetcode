class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        _sum = sum(nums)
        if _sum%k!=0:
            return False
        target = _sum/k
        visit = [0 for i in nums]
        
        nums = sorted(nums,reverse=True)
        def help(nums,k,index,sum,target,count):
            if k==1:
                return True
            if sum==target and count > 0:
                return help(nums,k-1,0,0,target,0)
            for i in range(index,len(nums)):
                if not visit[i] and sum+nums[i]<=target:
                    visit[i] = 1
                    if help(nums,k,i+1,sum+nums[i],target,count+1):
                        return True
                    visit[i] = 0
            return False
        return help(nums,k,0,0,target,0)
        