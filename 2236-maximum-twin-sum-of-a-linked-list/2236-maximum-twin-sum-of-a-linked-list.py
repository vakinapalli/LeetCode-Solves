# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a = b = head
        hold = []
        while b != None and b.next != None:
            hold.append(a.val)
            a = a.next
            b = b.next.next
        hold.pop
        for i in range(len(hold) - 1, -1, -1):
            hold[i] += a.val
            a = a.next
        return max(hold)
        
