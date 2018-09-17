class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        def help(r):
            if not r:
                return
            res.append(r.val)
            for i in r.children:
                help(i)
        help(root)
        return res