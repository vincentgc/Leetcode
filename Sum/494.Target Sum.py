class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        memory = {}
        def help(i,s):
            if (i,s) not in memory:
                r = 0
                if i==len(nums):
                    if s==0:
                        r = 1
                else:
                    r = help(i+1,s+nums[i])+help(i+1,s-nums[i])
                memory[(i,s)] = r
            return memory[(i,s)]
        return help(0,S)
        