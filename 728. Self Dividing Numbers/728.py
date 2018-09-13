class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
		#Time O(right-left)
        def help(num):
            origin = num
            while num > 0:
                temp = num % 10
                if temp == 0:
                    return False
                if origin%temp != 0:
                    return False
                num = num/10
                
            return True
        res = []
        for i in range(left,right+1):
            if help(i):
                res.append(i)
        return res