class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = range(1,10)
        res = []
        def help(nums,k,n,path,res):
            if len(path)==k and sum(path)==n:
                res.append(path)
                return 
            elif len(path)>k:
                return
            for i in range(len(nums)):
                help(nums[i+1:],k,n,path+[nums[i]],res)
        help(nums,k,n,[],res)
        return res