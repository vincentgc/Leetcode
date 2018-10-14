class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = [[root,root.val]]
        res = 0
        while stack:
            node,value = stack.pop()
            if not node.left and not node.right:
                res += value
            if node.left:
                stack.append([node.left,value*10+node.left.val])
            if node.right:
                stack.append([node.right,value*10+node.right.val])
        return res