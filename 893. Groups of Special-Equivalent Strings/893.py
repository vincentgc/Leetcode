class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def help(a):
            tmp1 = a[::2]
            tmp2 = a[1::2]
            tmp1,tmp2= sorted(tmp1),sorted(tmp2)
            return ''.join(tmp1)+''.join(tmp2)
        d = {}
        for i in range(len(A)):
            trans = help(A[i])
            d[trans] = d.get(trans,0)+1
        return len(d.keys())