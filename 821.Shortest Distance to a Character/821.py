class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        N = len(S)
        i = 0
		#先找出第一个C的位置
        while i < N:
            if S[i] == C:
                j = i
                break
            i += 1
        first = 0
        second = j
        res = []
        i = 0
		#从0开始计算，寻找first和second, 计算与first和second之间的距离，取最小值
		#两个边界条件需要考虑：
		#1.第一个元素就是C
		#2.最后一个元素是C或不是C
        while i < N:
            if first == 0 and S[0]!= C and i < second:
                res.append(second-i)
                i += 1
            elif i == second:
                first = second
                second += 1
                while second < N and S[second]!=C:
                    second += 1
                i += 1
                res.append(0)
            elif i > first and i < second:
                if second == N and S[second-1]!=C:
                    res.append(i-first)
                else:
                    res.append(min(i-first,second-i))
                i += 1
        return res

#更方便的版本，先列出C所在的位置，然后遍历比较
#Time O（N）-O（N2） 
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        index = [i for i,v in enumerate(S) if v == C]
        N = len(S)
        res = [N] * N
        for i in range(N):
            for j in index:
                res[i] = min(res[i],abs(j-i))
        return res