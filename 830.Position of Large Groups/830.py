class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        i,j = 0,0
        count = 1
        res = []
        while i < len(S):
			#注意边界条件
            if i!=len(S)-1 and S[i+1]==S[i]:
                count += 1
            elif i==len(S)-1 or S[i+1]!=S[i]:
                if count >= 3:
                    res.append([j,i])
                j = i + 1
                count = 1
            i += 1
        return res