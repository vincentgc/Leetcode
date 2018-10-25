class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [float('inf') for _ in range(amount)]
        
        for c in coins:
            for i in range(c,amount+1):
                dp[i] = min(dp[i],dp[i-c]+1)
        
        return dp[-1] if dp[-1]!=float('inf') else -1