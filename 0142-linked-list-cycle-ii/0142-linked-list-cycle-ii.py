# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = b = head
        
        cyc = False
        while b != None and b.next != None:
            a = a.next
            b = b.next.next
            if a == b:
                cyc = True
                break
        if not cyc:
            return None
        c = head
        while cyc and a != c:
            a = a.next
            c = c.next
        return c