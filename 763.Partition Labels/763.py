class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
		#先把字母出现的首位置和末位置存到字典中
        d = {}
        for i,v in enumerate(S):
            if v not in d:
                d[v] = [i,i]
            else:
                d[v][1] = i
		#按首位置顺序排序
        sort_d = sorted(d.items(),key=lambda x:x[1][0])
		#合并有交叉的部分
        res = [sort_d[0][1]]
        for i in range(1,len(sort_d)):
            if sort_d[i][1][0] < res[-1][1]:
                res[-1][1] = max(sort_d[i][1][1],res[-1][1])
            else:
                res.append(sort_d[i][1])
        final = []
        for i in res:
            final.append(i[1]-i[0]+1)
        return final