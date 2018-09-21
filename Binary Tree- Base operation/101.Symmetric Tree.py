class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
		#两次前序遍历，只是换下左右方向，判断遍历后是否相同
        res1 = []
        res2 = []
        def help1(node):
            if not node:
                res1.append('null')
                return
            res1.append(node.val)
            help1(node.left)
            help1(node.right)
        def help2(node):
            if not node:
                res2.append('null')
                return
            res2.append(node.val)
            help2(node.right)
            help2(node.left)
        help1(root)
        help2(root)
        return res1==res2