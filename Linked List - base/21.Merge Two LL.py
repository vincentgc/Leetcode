class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return
        elif l1 and not l2:
            return l1
        elif l2 and not l1:
            return l2
        else:
            if l1.val <= l2.val:
                l1.next = self.mergeTwoLists(l1.next,l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1,l2.next)
                return l2