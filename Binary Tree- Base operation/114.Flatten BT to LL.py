class Solution(object):
    prev = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        self.prev = root
        self.flatten(root.left)
        
        tmp = root.right
        root.right, root.left = root.left,None
        self.prev.right = tmp
        
        self.flatten(tmp)
        