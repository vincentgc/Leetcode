class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def help(n,index,k,path,res):
            if len(path)==k:
                res.append(path)
                return
            else:
                for i in range(index,n+1):
                    help(n,i+1,k,path+[i],res)
        help(n,1,k,[],res)
        return res
                    