class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.left and root.right:
            return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
        elif root.left:
            return self.hasPathSum(root.left,sum-root.val)
        elif root.right:
            return self.hasPathSum(root.right,sum-root.val)
        else:
            return root.val==sum