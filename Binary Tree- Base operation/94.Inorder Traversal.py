class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def help(node):
            if not node:
                return node
            
            help(node.left)
            res.append(node.val)
            help(node.right)
        help(root)
        return res