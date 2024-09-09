# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        a= ListNode()
        b = ListNode()
        c = ListNode()

        a = head
        b = head.next
        c = b.next
        a.next = None
        head.next = None
        while b != None:
            b.next = a
            a = b
            b = c
            if b != None:
                c = b.next
        return a

          
        