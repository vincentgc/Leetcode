def numJewelsInStones(self, J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
	#判断S中字符有多少出现在J中
    res = 0
    for s in S:
        if s in J:
            res += 1
    return res
	#一行写法
	#return sum(s in J for s in S)