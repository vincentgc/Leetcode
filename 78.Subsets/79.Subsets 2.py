class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        exist = set()
        def help(nums,index,path,res):
            #print path
            #print exist
            tmp = ''.join(sorted(str(path)))
            #print tmp
            if tmp not in exist:
                exist.add(tmp)
                res.append(path)
            for i in range(index,len(nums)):
                help(nums,i+1,path+[nums[i]],res)
        help(nums,0,[],res)
        return res