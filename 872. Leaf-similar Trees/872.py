class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        #DFS
        res = []
        def help(node):
            if not node:
                return
            if not node.right and not node.left:
                res.append(node.val)
            help(node.left)
            help(node.right)
        help(root1)
        res1 = res
        res = []
        help(root2)
        res2 = res
        return res1 == res2