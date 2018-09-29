class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def help(node,level):
            if not node:
                return
            while len(res) <= level:
                res.append([])
            res[level].append(node.val)
            help(node.left,level+1)
            help(node.right,level+1)
        help(root,0)
        return res