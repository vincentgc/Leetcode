class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a = A.split()
        b = B.split()
        d1,d2 = {},{}
        for i in a:
            d1[i] = d1.get(i,0)+1
        for j in b:
            d2[j] = d2.get(j,0)+1
        res = []
        for i in d1.keys():
            if d1[i] == 1 and i not in d2:
                res.append(i)
        for j in d2.keys():
            if d2[j] == 1 and j not in d1:
                res.append(j)
        return res