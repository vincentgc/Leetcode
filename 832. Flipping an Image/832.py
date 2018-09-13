def flipAndInvertImage(self, A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    #Time: O(n2)
    l = len(A[0])-1
    for i in range(len(A)):
        for j in range(len(A[0])/2):
            A[i][j],A[i][l-j] = A[i][l-j],A[i][j]
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = 1- A[i][j]
    return A