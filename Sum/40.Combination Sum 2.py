class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(candidates)
        res = []
        def help(nums,index,path,target,res):
            if target == 0:
                res.append(path)
                return
            for i in range(index,len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                if nums[i] <= target:
                    help(nums,i+1,path+[nums[i]],target-nums[i],res)
        help(nums,0,[],target,res)
        return res