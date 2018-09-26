class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def help(node):
            if not node:
                return 0
            left = help(node.left)
            right = help(node.right)
            res.append(right+left+node.val)
            return left+right+node.val
        res = []
        help(root)

        d = {}
        _max = 0
        final = []
        for i in res:
            d[i] = d.get(i,0)+1
            if d[i] > _max:
                final = [i]
                _max = d[i]
            elif d[i] == _max:
                final.append(i)
        return final