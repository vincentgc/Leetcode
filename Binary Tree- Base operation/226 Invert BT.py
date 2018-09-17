class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        root.left,root.right= self.invertTree(root.right),self.invertTree(root.left)
		#不要分开写
        return root