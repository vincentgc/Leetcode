import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = [(r[0],r,1) for r in matrix]
        heapq.heapify(heap)

        for _ in range(k-1):
            v,r,i = heap[0]
            if i < len(r):
                heapq.heapreplace(heap,(r[i],r,i+1))
            else:
                heapq.heappop(heap)
        return heap[0][0]
        