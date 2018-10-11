class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = {}
        start = result = max_len = 0
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0)+1
            max_len = max(max_len,d[s[i]])
            if i-start+1-max_len > k:
                d[s[start]] -= 1
                start += 1
            result = max(result,i-start+1)
        return result
        