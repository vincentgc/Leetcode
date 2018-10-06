class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        d = {}
        for i in hand:
            d[i] = d.get(i,0) + 1
        for j in sorted(d):
            if d[j] > 0:
                for i in range(W)[::-1]:
                    if i+j not in d:
                        d[i+j] = 0
                    d[i+j] -= d[j]
                    if d[i+j] < 0:
                        return False
        return True