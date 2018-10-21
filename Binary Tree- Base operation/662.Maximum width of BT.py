class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 1
        self.dfs(root,0,1,[])
        return self.res
    def dfs(self,node,level,index,start):
        if not node:
            return
        if len(start)==level:
            start.append(index)
        self.res = max(self.res, index-start[level]+1)
        self.dfs(node.left,level+1,index*2,start)
        self.dfs(node.right,level+1,index*2+1,start)
        