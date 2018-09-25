class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [[]]
        def help(node,level):
            if not node:
                return
            while len(res)<=level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                help(node.left,level+1)
            if node.right:
                help(node.right,level+1)
        help(root,0)
        return res[-1][0]