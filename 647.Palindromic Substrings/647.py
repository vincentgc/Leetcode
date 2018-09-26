class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for r in range(len(s)-1,-1,-1):
            for c in range(r+1,len(s)):
                if c==r+1:
                    if s[r]==s[c]:
                        dp[r][c]=1
                    else:
                        dp[r][c]=0
                else:
                    if s[r]==s[c] and dp[r+1][c-1]==1:
                        dp[r][c]=1
                    else:
                        dp[r][c]=0
        return sum([sum(row) for row in dp])