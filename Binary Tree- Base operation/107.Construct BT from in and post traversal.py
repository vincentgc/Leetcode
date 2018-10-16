class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        r_val = postorder[-1]
        r_idx = inorder.index(r_val)
        r_len = r_idx
        root = TreeNode(r_val)
        root.right = self.buildTree(inorder[r_idx+1:],postorder[r_len:-1])
        root.left = self.buildTree(inorder[:r_idx],postorder[:r_len])
        return root
        