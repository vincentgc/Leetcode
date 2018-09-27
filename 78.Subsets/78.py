class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def help(nums,index,path,res):
            res.append(path)
            for i in range(index,len(nums)):
                help(nums,i+1,path+[nums[i]],res)
        help(sorted(nums),0,[],res)
        return res
        