class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        d = {}
        length = sum(wall[0])
        for i in wall:
            s = 0
            for j in i:
                s += j
                if s!=length:
                    d[s] = d.get(s,0)+1
        _max = 0
        for p in d:
            _max = max(_max,d[p])
        return len(wall)-_max