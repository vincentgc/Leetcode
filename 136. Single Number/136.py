class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
		#两个相同数字异或后变为0
        res = 0
        for n in nums:
            res = res^n
        return res