class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        def help(pr,po):
            if len(pr)==0:
                return None
            if len(pr)==1:
                return TreeNode(pr[0])
            node = TreeNode(pr[0])
            index = pr.index(po[-2])
            l = len(post)
            node.left = help(pr[1:index],po[:index-1])
            node.right = help(pr[index:],po[index-1:-1])
            return node
        return help(pre,post)