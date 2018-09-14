class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
		#DFS
        if not root:
            return 0
        res = [0]
        for i in root.children:
            res.append(self.maxDepth(i))
        return max(res)+1