class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=="":
            return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        def help(digits,index,path,res):
            if len(path) == len(digits):
                res.append(''.join(path))
                return
            for i in range(index,len(digits)):
                for j in range(len(kvmaps[digits[i]])):
                    help(digits,i+1,path+[kvmaps[digits[i]][j]],res)
        help(digits,0,[],res)
        return res