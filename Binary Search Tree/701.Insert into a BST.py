class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return
        if root.val < val:
            if not root.right:
                root.right = TreeNode(val)
            else:
                root.right = self.insertIntoBST(root.right,val)
        elif root.val > val:
            if not root.left:
                root.left = TreeNode(val)
            else:
                root.left = self.insertIntoBST(root.left,val)
        return root	