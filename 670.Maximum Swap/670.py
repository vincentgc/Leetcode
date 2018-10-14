class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        res = num[:]
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                num[i],num[j] = num[j],num[i]
                if num > res:
                    res = num[:]
                num[j],num[i] = num[i],num[j]
        return int(''.join(res))
        