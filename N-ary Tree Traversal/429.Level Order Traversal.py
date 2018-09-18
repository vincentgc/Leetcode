class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = [[]]
        def help(node,level):
            if not node:
                return 
            while len(res) <= level:
                res.append([])
            res[level].append(node.val)
            for i in node.children:
                help(i,level+1)
        help(root,0)
        return res