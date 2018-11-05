class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        def help(node,path,res):
            if not node.left and not node.right:
                res.append(path + str(node.val))
                return
            if node.left:
                help(node.left,path+str(node.val)+'->',res)
            if node.right:
                help(node.right,path+str(node.val)+'->',res)
        help(root,"",res)
        return res