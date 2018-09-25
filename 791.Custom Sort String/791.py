class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
		#先讲S中的排序
        d = {}
        for i,v in enumerate(S):
            d[v] = i
        sort_d = sorted(d.items(),key=lambda x:x[1])
        #再看T中，分出没在S中的字母和在S中字母的个数
		d2 = {}
        no_tmp = ''
        for j in T:
            if j not in d:
                no_tmp += j
            else:
                d2[j] = d2.get(j,0)+1
        #合并
		tmp = ''
        for p in sort_d:
            if p[0] in d2:
                tmp += p[0]*d2[p[0]]
        return tmp + no_tmp       