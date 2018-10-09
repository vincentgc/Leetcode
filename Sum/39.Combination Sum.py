class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def help(nums,target,path,res):
            if target<0:
                return
            elif target==0:
                res.append(path)
            else:
                for i in range(len(nums)):
                    help(nums[i:],target-nums[i],path+[nums[i]],res)
        res = []
        help(candidates,target,[],res)
        return res
        