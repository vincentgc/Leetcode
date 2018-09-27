class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = [0]
        _k = [k]
        def help(node,k):
            if not node:
                return
            help(node.left,k)
            k[0] = k[0]-1
            if k[0] == 0:
                res[0] = node.val
            help(node.right,k)
        help(root,_k)
        return res[0]