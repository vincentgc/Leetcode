class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        def help(nums,length,tmp,res):
            if len(tmp)==length:
                res.append(tmp)
                return
            for i in range(len(nums)):
                help(nums[:i]+nums[i+1:],length,tmp+[nums[i]],res)
        res = []
        help(nums,length,[],res)
        return res