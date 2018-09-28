class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
		#注意排序是按x[1]排，不是按x[0]，这是种贪心算法
        sort_pair = sorted(pairs,key=lambda x:x[1])
        #print sort_pair
        cur = float('-inf')
        res = 0
        for i in sort_pair:
            if i[0] > cur:
                cur = i[1]
                res += 1
        return res