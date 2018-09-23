class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        flag = False
        for i,v in enumerate(nums):
            if v not in d:
                d[v] = i
            else:
                flag = ((d[v] + k) >= i)
                if flag == True:
                    return True
                d[v] = i
        return False