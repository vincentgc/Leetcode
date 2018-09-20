class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        def help(node):
            if not node:
                return 0
            else:
                left = help(node.left)
                right = help(node.right)
                print left,right
                res[0] = res[0] + abs(left-right)
				#注意这个返回值
                return node.val+left+right
        help(root)
        return res[0]