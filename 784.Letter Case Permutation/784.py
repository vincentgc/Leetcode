class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
		#典型回溯题,但是回溯特别特别特别费时，尽量不要用
        length = len(S)
        def dfs(S,index,temp,length,res):
            if index == length:
                res.append(temp)
            for i in range(len(S)):
                if S[i].isalpha():
                    dfs(S[i+1:],index+1,temp+S[i].lower(),length,res)
                    dfs(S[i+1:],index+1,temp+S[i].upper(),length,res)
                else:
                    dfs(S[i+1:],index+1,temp+S[i],length,res)
        res = []
        dfs(S,0,'',length,res)
        return res
	def another(self,S):
		#这个方法要快10倍
		res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i+ch for i in res]
        return res