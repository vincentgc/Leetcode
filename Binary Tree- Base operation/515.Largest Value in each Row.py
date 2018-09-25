class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        def help(node,level):
            if not node:
                return
            while len(res)<=level:
                res.append(float('-inf'))
            res[level] = max(node.val,res[level])
            if node.left:
                help(node.left,level+1)
            if node.right:
                help(node.right,level+1)
        help(root,0)
        return res