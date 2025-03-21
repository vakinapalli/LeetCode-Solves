# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head and head.next:
            p2 = p1 = head
            p2 = p2.next
            while p2.next and p2.next.next:
                if p2 == p1:
                    return True
                p1 = p1.next
                p2 = p2.next.next
            
            
        return False
        