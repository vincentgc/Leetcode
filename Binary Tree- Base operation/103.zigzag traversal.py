class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return []
        def help(node,level):
            if not node:
                return
            if len(res) <= level:
                res.append([])
            res[level].append(node.val)
            help(node.left,level+1)
            help(node.right,level+1)
        help(root,0)
        for i in range(len(res)):
            if i%2==1:
                res[i] = res[i][::-1]
        return res