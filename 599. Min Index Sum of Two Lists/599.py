class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}
        for i,v in enumerate(list1):
            d[v] = [i]
        for j,m in enumerate(list2):
            if m in d:
                d[m].append(j)
        _min = len(list1) + len(list2)
        res = []
        for p in d.keys():
            if len(d[p]) == 2:
                if sum(d[p]) < _min:
                    res = [p]
                    _value = p
                    _min = sum(d[p])
                elif sum(d[p]) == _min:
                    res.append(p)
        return res