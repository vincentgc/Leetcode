class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = {}
        words = sorted(words)
        print words
        for w in words:
            d[w] = d.get(w,0)+1
        sort_d = sorted(d,key=lambda w:(-d[w],w))
        print sort_d
        return sort_d[:k]
            