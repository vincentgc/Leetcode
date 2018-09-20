class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s1 = []
        s2 = []
        for i in S:
            if i=='#' and s1:
                s1.pop()
            elif i!='#':
                s1.append(i)
        for j in T:
            if j=='#' and s2:
                s2.pop()
            elif j!='#':
                s2.append(j)
        print s1,s2
        return s1==s2