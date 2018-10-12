class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def help(nums,index,path,res):
            exist = set()
            if len(path)>1:
                res.append(path)
            for i in range(index,len(nums)):
                if not path or nums[i] >= path[-1]:
                    if nums[i] not in exist:
                        help(nums,i+1,path+[nums[i]],res)
                        exist.add(nums[i])
        help(nums,0,[],res)
        return res
        