class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        res = [None]
        def dfs(r):
            if not r:
                return None
            if r.val == val:
                res[0] = r
            dfs(r.left)
            dfs(r.right)
        dfs(root)
        return res[0]