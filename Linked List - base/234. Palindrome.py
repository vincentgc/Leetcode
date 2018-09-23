class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        value = []
        value.append(head.val)
        while head.next:
            head = head.next
            value.append(head.val)
        return value == value[::-1]