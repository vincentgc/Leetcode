class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        r_val = preorder[0]
        #print inorder
        r_idx = inorder.index(r_val)
        r_len = r_idx
        root = TreeNode(r_val)
        root.left = self.buildTree(preorder[1:1+r_len],inorder[:r_idx])
        root.right = self.buildTree(preorder[1+r_len:],inorder[r_idx+1:])
        return root