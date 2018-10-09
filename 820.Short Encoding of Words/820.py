class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len, reverse=True)
        words = [word + '#' for word in words]
        S =''
        for word in words:
            if word not in S:
                S += word
        return len(S)