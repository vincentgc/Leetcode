class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def help(node):
            if not node:
                return node,0
            left,leftsum = help(node.left)
            right,rightsum = help(node.right)
            if leftsum == 0:
                node.left = None
            if rightsum == 0:
                node.right = None
            return node,node.val+rightsum+leftsum
        res,_ = help(root)
        return res