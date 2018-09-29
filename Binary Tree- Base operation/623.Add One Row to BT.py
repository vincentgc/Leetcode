class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        def help(node,level,v,d):
            if not node:
                return 
            if level==d-1:
                #if node.left:
                tmp = node.left
                insert = TreeNode(v)
                node.left = insert
                insert.left = tmp
                #if node.right:
                tmp1 = node.right
                insert1 = TreeNode(v)
                node.right = insert1
                insert1.right = tmp1
            help(node.left,level+1,v,d)
            help(node.right,level+1,v,d)
        if d == 1:
            tmp = TreeNode(v)
            tmp.left = root
            return tmp
        else:
            help(root,1,v,d)
            return root