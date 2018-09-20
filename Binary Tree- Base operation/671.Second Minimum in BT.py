class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [root.val,root.val]
        def help(node):
            if not node:
                return 
            if res[1]==res[0] and node.val>res[0]:
                res[0] = node.val
            if node.val < res[0] and node.val>res[1]:
                res[0] = node.val
            elif node.val < res[1]:
                res[0] = res[1]
                res[1] = node.val
            help(node.left)
            help(node.right)
        help(root)
        if res[0] == res[1]:
            return -1
        else:
            return res[0]