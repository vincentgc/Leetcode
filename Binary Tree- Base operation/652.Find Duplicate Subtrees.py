# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        d = {}
        
        def help(node):
            if not node:
                return '#'
            tmp = help(node.left)+help(node.right)+str(node.val)
            if tmp in d and d[tmp] == 1:
                res.append(node)
            d[tmp] = d.get(tmp,0)+1
            return tmp
        
        help(root)
        return res