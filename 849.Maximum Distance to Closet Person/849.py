class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
		#转化为求两个1之间的距离
        index = []
        for i in range(len(seats)):
            if seats[i] == 1:
                index.append(i)
        _max = 0
        for j in range(len(index)-1):
            _max = max(index[j+1]-index[j],_max)
		#考虑头尾的状况
        _max = max(_max/2,index[0]-0,len(seats)-index[-1]-1)
        return _max