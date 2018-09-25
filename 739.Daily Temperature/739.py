class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i,v in enumerate(temperatures):
            while stack and v > stack[-1][1]:
                f = stack.pop()
                res[f[0]] = i - f[0]
            stack.append((i,v))
        return res