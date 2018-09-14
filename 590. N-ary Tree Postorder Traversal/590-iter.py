class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            temp = stack.pop()
            res.append(temp.val)
            [stack.append(x) for x in temp.children]
        return res[::-1]