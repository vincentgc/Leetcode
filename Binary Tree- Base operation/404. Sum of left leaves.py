class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        def help(node):
            if not node:
                return
			#找左叶
            if node.left and not node.left.left and not node.left.right:
                res[0] = res[0]+node.left.val
            help(node.left)
            help(node.right)
        help(root)
        return res[0]