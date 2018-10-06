class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def help(node,level):
            if not node:
                return node
            if len(res)<=level:
                res.append([])
            res[level].append(node.val)
            help(node.left,level+1)
            help(node.right,level+1)
        help(root,0)
        final = []
        for i in res:
            final.append(i[-1])
        return final