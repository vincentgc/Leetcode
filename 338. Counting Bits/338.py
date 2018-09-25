class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0 for _ in range(num+1)]
        j = 1
        for i in range(1,num+1):
			#是2的指数则1的数量肯定为1
            if i==2**j:
                dp[i] = 1
                j += 1
            else:
                dp[i] = dp[i-1]+1
                tmp = i
				#根据i与2的倍数关系调整dp
                while tmp%2 == 0:
                    dp[i] = dp[i] - 1
                    tmp = tmp/2
        return dp