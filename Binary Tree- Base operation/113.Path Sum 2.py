class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        
        def help(node,target,path,res):
            if not node:
                return
            if not node.left and not node.right and target==node.val:
                path.append(node.val)
                res.append(path)
                return
            if node.left:
                help(node.left,target-node.val,path+[node.val],res)
            if node.right:
                help(node.right,target-node.val,path+[node.val],res)
        help(root,sum,[],res)
        return res
        