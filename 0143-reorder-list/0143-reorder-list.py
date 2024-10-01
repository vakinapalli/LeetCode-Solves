# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        a = head
        nodes = []
        while a != None:
            nodes.append(a)
            h = a
            a = a.next
            h.next = None
        x = 0
        y = len(nodes) - 1
        dum = ListNode()
        b = dum
        while x < y:
            b.next = nodes[x]
            b = b.next
            b.next = nodes[y]
            b = b.next
            x += 1
            y -= 1
        if x == y:
            b.next = nodes[x]
        return dum.next


        