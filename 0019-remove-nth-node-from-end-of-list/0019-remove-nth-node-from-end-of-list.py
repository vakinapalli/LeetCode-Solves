# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        a = head
        l = 0
        b = a
        d = None
        while a != None:
            l += 1
            d = b
            b = a
            a = a.next
        if n == l:
            return head.next
        if n == 1:
            d.next = None
            return head
        c = head
        for i in range(l - n - 1):
            c = c.next
        c.next = c.next.next
        return head
