class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        exist = set()
        res = 0
        _max = 0
        for i in range(len(nums)):
            tmp = i
            if tmp in exist:
                continue
            else:
                while tmp not in exist:
                    res += 1
                    exist.add(i)
                    tmp = nums[tmp]
                _max = max(_max,res)
                res = 0
        return _max
                