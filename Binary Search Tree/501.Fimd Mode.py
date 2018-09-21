class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
		#先遍历再找出现最多的数，有优化空间
        res = []
        def help(node):
            if not node:
                return 
            res.append(node.val)
            help(node.left)
            help(node.right)
        help(root)
        _max = 0
        d = {}
        print res
        _value = []
        for i in res:
            d[i] = d.get(i,0)+1
            if _max < d[i]:
                _value = [i]
                _max = d[i]
            elif _max == d[i]:
                _value.append(i)
        return _value