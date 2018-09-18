class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A)!=len(B):
            return False
        if not A and not B:
            return True
        index = [i for i,v in enumerate(B) if v == A[0]]
        for i in index:
            if (B[i:] + B[:i]) == A:
                return True
        return False
        #one sentence:
        #return (len(A)==len(B)) and (B in A+A)