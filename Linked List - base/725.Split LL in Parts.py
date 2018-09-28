class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if not root:
            return [[] for _ in range(k)]
        #计算链表长度
		tmp = root
        l = 1
        while tmp.next:
            tmp = tmp.next
            l += 1
		#根据总长分配每一部分长度
        base = l//k
        rest = l%k
        res = [base for _ in range(k)]
        for i in range(rest):
            res[i] = res[i] + 1
        #根据每一部分长度分割链表
        curr = root
        final = []
        for i in range(len(res)):
            if res[i] == 0:
                final.append([])
            else:
                prev = curr
                tmp_list = prev
                tmp = res[i]
                while tmp > 1:
                    prev = prev.next
                    tmp -= 1
                curr = prev.next
                prev.next = None
                final.append(tmp_list)
        return final
            