class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
		#注意等号
        res = ''
        if num > 0:
            tmp = num
        elif num == 0:
            return '0'
        else:
            tmp = num * -1
            res += '-'
        i = 0
        while 7**i <= tmp:
            i += 1
        j =  i - 1
        print j
        print tmp
        while tmp >= 0 and j >= 0:
            p = 0
            while tmp >= 7**j*p:
                p += 1
            res += str(p-1)
            tmp -= (p-1)*(7**j)
            j -= 1
        return res