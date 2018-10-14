class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        def help(nums,index,n,path,res):
            if index==n and path not in res:
                res.append(path)
                return
            for i in range(len(nums)):
                help(nums[:i]+nums[i+1:],index+1,n,path+[nums[i]],res)
        help(nums,0,n,[],res)
        return res