class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        def help(node):
            if not node:
                return
            for i in node.children:
                help(i)
            res.append(node.val)
        help(root)
        return res