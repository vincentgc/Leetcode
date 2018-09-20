class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
		#转化为求解树的最大深度的问题
        if not root:
            return 0
        res = [0]
        def helper(node):
            if not node:
                return 0
            l = helper(node.left)
            r = helper(node.right)
            res[0] = max(res[0],l+r+1)
            return max(l,r)+1
        helper(root)
        return res[0]-1