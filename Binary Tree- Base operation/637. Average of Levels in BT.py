class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
		#用的DFS，也可以用BFS，会更方便一点
        res = [[]]
        def help(node,level):
            if not node:
                return
            while len(res)<=level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                help(node.left,level+1)
            if node.right:
                help(node.right,level+1)
        help(root,0)
        final = []
        for l in res:
            final.append(sum(l)/float(len(l)))
        return final