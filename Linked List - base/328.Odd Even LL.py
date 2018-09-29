class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        odd = dummy1
        even = dummy2
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = dummy2.next
        return dummy1.next
        