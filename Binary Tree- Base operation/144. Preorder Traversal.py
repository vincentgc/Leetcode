class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def help(node):
            if not node:
                return node
            res.append(node.val)
            help(node.left)
            help(node.right)
        res = []
        help(root)
        return res